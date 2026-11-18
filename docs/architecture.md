---
layout: default
title: Architecture
---

[Documentation home](index.md) · [Workloads and execution](execution.md) · [Roadmap](roadmap.md)

# Architecture

Koinodos is designed to operate virtual PLCs and supporting services across industrial PCs. It coordinates placement, installation, application deployment, and diagnostics. The controller executes the control loop locally and owns its behavior when communications fail. A loss of the Koinodos control plane or its connection to a node must not by itself stop running controller logic.

## Components and responsibilities

![Koinodos scheduler, execution agent, and vendor adapter responsibilities](assets/architecture.svg)

| Component | Responsibility |
| --- | --- |
| **Control plane** | Stores desired workload state, inventory, and the operation history. Authorizes changes, selects the placement path, and presents observed state with its timestamp and source. |
| **Cluster scheduler** | Assigns workload tasks to suitable nodes based on capacity and constraints. Direct reuse of SwarmKit is the leading candidate. The Docker prototype will test the scheduling path for container workloads. |
| **Node agent and executors** | Report capabilities, confirm that assigned resources can be reserved, and manage execution through the selected backend. Reconcile local processes, containers, or VMs after restart. |
| **Vendor adapters** | Translate controller operations to the vendor's supported interfaces. Report available actions and observed application state. An adapter can run on the node or on a reachable gateway. |
| **Artifact store** | Holds versioned runtime images and native application packages by immutable identity and digest. Existing registries or storage services can provide the underlying storage. |
| **Operator interface** | Exposes inventory, deployment intent, progress, diagnostics, and audit history. It uses the control-plane API and displays actions supported by the target. |

The orchestration agent is outside the real-time path. The control plane issues workload and deployment requests, while the controller retains local access to its drivers, I/O, and application state.

## Workload and controller identity

A **workload release** identifies a version of a runtime or supporting service. It points to one or more compatible execution artifacts. A **workload instance** describes where and how that release should execute, with an explicit backend and required resources. The same industrial PC can run several workload instances.

A **controller target** is the endpoint on which an adapter performs PLC operations. Its identity survives backend restarts and is separate from a container ID, VM process ID, or temporary IP address. An **application package** is a native vendor artifact with a version, digest, and declared target compatibility. It has its own lifecycle, independent of the runtime release.

The UI reports three observations independently: the execution backend is running, the runtime endpoint is reachable, and the requested PLC application is active. A timestamp and source accompany each observation. Where the vendor interface cannot confirm an application version, the UI reports that limit explicitly.

## Deployment flow

1. An operator requests a workload release or application package for a specific target. The control plane records the intended state and checks permissions.
2. For a new runtime instance, the scheduler selects an eligible node. The node agent confirms resources and starts the selected backend. It reports the execution state and endpoint identity.
3. The adapter checks the target's supported operations, package compatibility, and preconditions such as a required stop or maintenance window.
4. The adapter invokes the vendor's deployment interface. The control plane tracks the operation by a stable ID through any retry or reconnect.
5. The adapter reads back the active application revision and operating state when the vendor exposes them. Observed results determine whether the operation succeeded.

**AnyPLC example.** A test cell can run an AnyPLC release in a Docker container. An isolated test cell can request the same compatible release under Kata. The AnyPLC adapter still deploys the native package produced by AnyPLC engineering tools. It exposes narrower operations such as Resource or Application deploy only where the runtime contract supports them.

An adapter can integrate additional controllers through an official API, SDK, CLI, or gateway. An already installed PLC can be enrolled as an external target, with lifecycle ownership staying with its existing host or vendor tooling. Vendor-specific diagnostics remain available alongside common identity, reachability, and status fields.

## Disconnects and recovery

- **Control-plane or agent disconnected.** Existing control logic continues locally. Observations are marked stale. New state-changing operations wait for an eligible, reachable executor.
- **Agent restarts.** It reconciles the assignment and the actual local runtime by stable identity. It can adopt the assigned instance when verified and reports conflicting evidence for resolution.
- **Deployment request times out.** The outcome is unknown until the adapter reads back current state or obtains authoritative evidence from the vendor. A repeat request uses the same operation ID where possible.
- **Node unavailable.** A portable workload can follow its configured recovery policy. A PLC with exclusive physical I/O requires confirmed release of the resource or an independently enforced mechanism that removes the former instance's access before another receives it.
- **Rollback requested.** The platform distinguishes reverting a runtime release from rolling back a PLC application and its state. The adapter advertises application rollback only where the vendor supports and verifies it.

## Trust boundaries

The node agent uses an authenticated, encrypted connection to the control plane. Enrollment establishes a unique node identity. Access to infrastructure management and PLC operations is scoped separately. The control plane records the actor, target, artifact identity, and outcome of state-changing requests.

The executor verifies artifact digests and uses scoped access to the runtime backend. Docker and Firecracker management interfaces stay on the trusted side of the node boundary. Vendor credentials are scoped to their target and capabilities. Secrets stay out of workload manifests and logs.

## Industry references

Where applicable and feasible, Koinodos will follow principles from [OPAF](https://www.opengroup.org/forum/open-process-automation-forum) and [Margo](https://docs.margo.org/). We will draw on OPAF and O-PAS for modular interfaces and interoperability, and on Margo for edge workload and device lifecycle management. As the implementation matures, we will document where it aligns with specific published requirements.

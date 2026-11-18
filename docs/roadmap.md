---
layout: default
title: Roadmap
---

[Documentation home](index.md) · [Architecture](architecture.md) · [Workloads and execution](execution.md)

# Roadmap

Koinodos starts with a small set of architecture documents. Later milestones describe the planned sequence of validation and implementation.

| Stage | Outcome |
| --- | --- |
| **1. Foundation and scheduler experiment** | Document system boundaries and the execution model. Demonstrate a container and Firecracker microVM assigned by the same SwarmKit scheduler and record the decision. |
| **2. Execution and agent contract** | Stabilize workload identity, capabilities, admission, and recovery behavior. Qualify a Kata execution path. |
| **3. First AnyPLC workflow** | Enroll a runtime, deploy a native application package, and verify the active revision and runtime state on a test target. |
| **4. Multi-vendor operation** | Connect a second PLC technology through a supported interface and verify that the core workload and operation contracts accommodate it. |
| **5. Industrial pilot** | Verify site operation, upgrades, backup and restore, failure handling, and the applicable real-time and physical I/O profiles. |

## Scheduler decision criteria

The proposed lab has one SwarmKit manager and two workers. At least one worker can run Firecracker. Start a regular OCI workload and a microVM workload using the same scheduler, then examine:

1. **Placement.** The microVM is assigned only to an eligible worker. Requests that cannot be placed explain what requirement is missing.
2. **Lifecycle.** Task identity can be traced to the assigned worker and backend instance. Stop releases reserved resources.
3. **Agent recovery.** Restarting the agent reconciles an existing workload without starting a duplicate.
4. **Upstream integration.** The experiment records the pinned upstream revision, integration points, and any required modifications. This evidence informs the choice between SwarmKit directly and Docker Swarm with explicit Firecracker placement.

The lab validates scheduling and execution boundaries. Product readiness, real-time behavior, and production I/O transfer are separate milestones.

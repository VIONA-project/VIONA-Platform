# Project overview

**VIONA — Virtualized Industrial Orchestration & Node Automation**

Software-defined automation needs a common way to deploy and operate virtual PLCs from different vendors across industrial sites. VIONA is an open-source project to build that platform for system integrators and industrial end users.

## What we are building

The goal is to give automation engineers a way to manage an entire fleet without specialist knowledge of orchestration, containers, or virtual machines. The platform will bring together deployment, updates, operating data, and controller diagnostics.

VIONA separates workload orchestration from controller operations. The control plane coordinates workloads, node agents manage their execution, and vendor connectors translate application deployment and diagnostic requests into supported controller interfaces. The controller retains ownership of its local control loop and I/O.

See the [architecture](architecture.md) for the proposed components, communication paths, and recovery behavior.

## Why open development

The platform's design affects how easily plant owners can change suppliers and how independently they can assess the security of operations. Open development lets plant owners, integrators, vendors, and individual contributors review the design and help shape it.

We will build on existing open-source orchestration and runtime components. Where applicable and feasible, we will follow principles from [OPAF](https://www.opengroup.org/forum/open-process-automation-forum) and [Margo](https://docs.margo.org/).

## Current status

VIONA is at the **design stage**. The documentation describes the proposed architecture and planned work. It does not describe a released platform.

The first implementation milestone is a Docker prototype, followed by an MVP, evaluation of lightweight VMs, vendor integrations, and industrial pilots. See the [roadmap](roadmap.md).

## Join the project

We welcome automation engineers, system integrators, industrial end users, vPLC vendors, and specialists in virtualization, orchestration, and cybersecurity.

Read [Contributing](contributing.md) to share a use case, review a design, or improve the documentation.

---
layout: default
title: Roadmap
---

[Documentation home](index.md) · [Architecture](architecture.md) · [Workloads and execution](execution.md)

# Roadmap

| Stage | Outcome |
| --- | --- |
| **1. Form the team and finalize the architecture** | Bring together the initial team and agree on the architecture, the components to reuse, and the scope of the Docker MVP. |
| **2. Build the Docker prototype** | Use Docker containers to demonstrate that Koinodos can place, start, stop, and observe workloads on industrial edge nodes. Use the results to verify the design choices that affect the MVP. |
| **3. Build and test the MVP** | Put the Docker-based workflow together and verify it on a testbed with AnyPLC. Test deployment, fleet monitoring, controller diagnostics, and recovery. A successful MVP launch opens the next two workstreams. |
| **4. Evaluate lightweight VMs and integrate vendor vPLCs** | In parallel, test whether Koinodos can run vPLCs through Kata Containers and Firecracker, and work with vPLC vendors as they develop and test their own connectors against the platform's integration interface. |
| **5. Run industrial pilot projects** | Take the platform to pilot installations after the VM evaluation and vendor integration work. Validate deployment, upgrades, and recovery under site conditions, along with the real-time and physical I/O requirements that apply to each installation. |

## Software development lifecycle

We will introduce software development lifecycle (SDLC) practices throughout the project. During architecture work, we will review design decisions and record how they are made. As implementation begins, we will add code review, continuous integration, automated tests, and dependency and security checks. We will formalize release and change management and vulnerability handling as the project moves toward pilots.

# Koinodos

**Open Industrial Orchestration**

Software-defined automation can only scale across industrial sites if engineers have a common way to deploy and operate virtual PLCs (vPLCs) from different vendors. Koinodos is an open-source project to build that platform for system integrators and industrial end users. The goal is to give automation engineers a way to manage an entire fleet without specialist knowledge of orchestration, containers, or virtual machines, with detailed operating data for each controller and the tools to diagnose faults.

The same platform will govern how controllers are deployed, updated, and accessed across a plant. Its design therefore affects how easily plant owners can change suppliers and how independently they can assess the security of those operations. We are developing Koinodos in the open so that plant owners and integrators can review the design and that individuals and companies can help shape it.

We will build on existing open-source orchestration and runtime components. In defining how those components work with controllers from different vendors, we will follow principles from the Open Process Automation Forum (OPAF) and the Margo initiative where they are applicable and feasible to implement.

## About the name

The name Koinodos combines *koinon* (κοινόν), a Greek term for a league of city-states, with *proodos* (πρόοδος), meaning progress. It reflects our aim to bring vPLC vendors together around an open platform and move industrial automation forward.

## Project status

Koinodos is at the design stage. We are publishing our initial vision and roadmap to give contributors a starting point.

We invite automation engineers, system integrators, industrial end users, vPLC vendors, and specialists in virtualization, orchestration, and cybersecurity to take part in the project. Individuals and companies can contribute by sharing requirements from industrial sites, helping shape the architecture, building the platform and its integrations, or testing early releases. [Open an issue](https://github.com/Koinodos-project/Koinodos-Platform/issues) to share a use case, propose a change, or tell us how you’d like to contribute.

| Read | What it covers |
| --- | --- |
| [Documentation home](docs/index.md) | Start here |
| [Architecture](docs/architecture.md) | Components, deployment and recovery flows, and trust boundaries |
| [Workloads and execution](docs/execution.md) | Docker, Kata Containers, Firecracker, and placement |
| [Roadmap](docs/roadmap.md) | Design, prototype, and pilot milestones |

## License

This repository is licensed under the [Apache License, Version 2.0](LICENSE). Integrated products and third-party components retain their own licenses.

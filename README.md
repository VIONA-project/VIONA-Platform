# Koinodos

**Open Industrial Orchestration**

Software-defined automation depends on a common way to deploy and operate virtual PLCs (vPLCs) from different vendors at industrial scale. Koinodos is our proposal for that platform. We want to make that work practical for system integrators and industrial end users. Automation engineers should be able to manage a fleet of vPLCs without needing specialist knowledge of orchestration, containers, or virtual machines. They should have access to detailed operating data for each controller and the tools to diagnose faults when they arise. We will build on existing open-source orchestration and runtime components and focus Koinodos on the requirements of industrial vPLC fleets.

The orchestration layer governs how controllers are deployed, updated, and accessed across a plant. Plant owners need to be able to change suppliers and verify how these operations are secured. We are developing Koinodos in the open so that plant owners and integrators can review those mechanisms, and individual contributors and companies can help design and build the platform.

Where applicable and feasible, we will follow principles from the Open Process Automation Forum (OPAF) and the Margo initiative as we design and build Koinodos.

## About the name

The name Koinodos combines *koinon* (κοινόν), a Greek term for a league of city-states, with *proodos* (πρόοδος), meaning progress. It captures the idea of moving industrial automation forward together.

## Project status

Koinodos is at the design stage. We are publishing our initial vision and roadmap and inviting automation engineers, integrators, end users, and vendors to review them. If you have a requirement from a real installation or see a gap in the design, [open an issue](https://github.com/Koinodos-project/Koinodos-Platform/issues). We also welcome contributors who want to help build the platform as the design takes shape. AnyPLC is the first planned integration.

| Read | What it covers |
| --- | --- |
| [Documentation home](docs/index.md) | Start here |
| [Architecture](docs/architecture.md) | Components, deployment and recovery flows, and trust boundaries |
| [Workloads and execution](docs/execution.md) | Docker, Kata Containers, Firecracker, and placement |
| [Roadmap](docs/roadmap.md) | Design, prototype, and pilot milestones |

## License

This repository is licensed under the [Apache License, Version 2.0](LICENSE). Integrated products and third-party components retain their own licenses.

# Koinodos

**Open Industrial Orchestration**

Software-defined automation depends on a common way to deploy and operate virtual PLCs (vPLCs) from different vendors at industrial scale. Koinodos is our proposal for that platform. We want to make that work practical for system integrators and industrial end users. Automation engineers should be able to manage a fleet of vPLCs without needing specialist knowledge of orchestration, containers, or virtual machines. They should have access to detailed operating data for each controller and the tools to diagnose faults when they arise. We plan to build on existing software and develop the platform with the automation community.

An orchestrator becomes part of the infrastructure a plant depends on. Its design affects whether users can change vendors and how they assess and manage cybersecurity risks. We believe infrastructure this important should be developed as open source, with both individuals and companies able to review the design and contribute.

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

# Koinodos

**Open Industrial Orchestration**

Koinodos is an open-source industrial orchestration platform designed to deploy, manage, and monitor virtual PLCs from multiple vendors in Docker containers and lightweight virtual machines. It is intended for integrators, machine builders, and operations teams that manage workloads across industrial edge nodes.

Vendor adapters connect controllers to a common management interface while preserving native engineering tools and application formats. Control logic runs locally on each PLC.

## Project status

Koinodos is in architecture design. The documentation describes intended behavior and the experiments required to validate it. The first integration target is AnyPLC.

| Read | What it covers |
| --- | --- |
| [Documentation home](docs/index.md) | Start here |
| [Architecture](docs/architecture.md) | Components, deployment and recovery flows, and trust boundaries |
| [Workloads and execution](docs/execution.md) | Docker, Kata Containers, Firecracker, and placement |
| [Roadmap](docs/roadmap.md) | Design, prototype, and pilot milestones |

## License

This repository is licensed under the [Apache License, Version 2.0](LICENSE). Integrated products and third-party components retain their own licenses.

# Workloads and execution

VIONA treats a virtual PLC as a workload with an explicit execution backend. The same runtime release can be packaged for different backends. Supported combinations are determined by the release, the node, and the target's requirements.

| Planned backend | Launch artifact | Execution environment |
| --- | --- | --- |
| **Host container** | OCI image | A Docker container using the host kernel. |
| **Kata Containers** | Compatible OCI image | A container inside a virtual machine with its own guest kernel. |
| **Direct Firecracker** | Compatible guest kernel and filesystem image | A Firecracker microVM containing the virtual PLC workload. |

The container and Kata variants may share an OCI image. Direct Firecracker needs a bootable guest artifact tied to the same release. The release records artifact digests and compatible architectures. [OCI](https://opencontainers.org/about/overview/) specifies container image, distribution, and runtime formats. [Compose](https://docs.docker.com/compose/) describes services, networks, and volumes for a local development stack. Architecture and placement requirements are expressed at the workload level.

## Scheduling and backend integration

The leading design uses [SwarmKit](https://github.com/moby/swarmkit) directly as the common cluster scheduler for heterogeneous tasks. A node-side executor maps an assigned workload to Docker, a Kata-capable runtime, or Firecracker. The Docker prototype will test the container path. After the Docker-based MVP is running and tested, the Kata and Firecracker evaluation will check which upstream interfaces can be reused and what integration code VIONA needs.

The alternative is Docker Swarm for supported container workloads and a VIONA agent managing Firecracker on explicitly assigned nodes. The architecture decision will compare placement ownership, recovery behavior, and maintenance cost. Integration with Kata remains subject to runtime and node qualification on either path.

## Placement and local admission

A workload may require a CPU architecture, a particular backend, CPU and memory capacity, or access to a dedicated network interface or I/O path. The scheduler first filters nodes by hard requirements, then chooses among the remaining candidates. A request stays pending if the requested backend or isolation level cannot be satisfied.

The node agent has the final view of resources that can actually be acquired on its host. It confirms local allocation before execution. Each exclusive resource has a single owner, and assignment alone does not grant access. Failed local admission remains visible with a reason and releases partial allocations.

Examples of deployment profiles:

| Profile | Placement and recovery |
| --- | --- |
| **Simulation** | Any eligible node with sufficient capacity. Automatic restart is possible where state and storage permit it. |
| **Isolated test cell** | A qualified Kata or Firecracker node. Recovery preserves the requested isolation. |
| **PLC with dedicated I/O** | A qualified node with exclusive access to the device, reserved CPU resources, and an explicit recovery policy. A replacement receives I/O access only after ownership is resolved. |

Real-time and fieldbus behavior will be qualified for the exact combination of host and guest kernels, runtime, device access, CPU allocation, and hardware. Container or VM availability alone does not establish timing or I/O suitability. Runtime and application updates are qualified independently.

## Backend references

- [SwarmKit task lifecycle](https://github.com/moby/swarmkit/blob/master/design/task_model.md)
- [SwarmKit scheduler design](https://github.com/moby/swarmkit/blob/master/design/scheduler.md)
- [Kata Containers installation and runtime integration](https://github.com/kata-containers/kata-containers/blob/main/docs/installation.md)
- [Firecracker guest kernel and filesystem requirements](https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md)

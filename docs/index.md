# VIONA Documentation

```{raw} html
<p class="viona-intro">Open Industrial Orchestration — a common way to deploy and operate virtual PLCs across industrial sites.</p>
```

Welcome to the VIONA documentation. VIONA stands for **Virtualized Industrial Orchestration & Node Automation**. We are building an open platform for automation engineers, system integrators, and industrial end users working with controllers from different vendors.

```{note}
**Design-stage documentation.** These pages describe the proposed architecture and roadmap. The platform is not yet released, and interfaces will evolve as the prototype is built and tested.
```

## Explore the documentation

```{raw} html
<div class="viona-topics">
  <article class="viona-topic">
    <h3><a href="overview.html">Project overview</a></h3>
    <p>Understand the goals, design principles, and current status of VIONA.</p>
  </article>
  <article class="viona-topic">
    <h3><a href="architecture.html">Architecture</a></h3>
    <p>Explore components, deployment flows, communication paths, and trust boundaries.</p>
  </article>
  <article class="viona-topic">
    <h3><a href="infrastructure-lifecycle.html">Infrastructure lifecycle management</a></h3>
    <p>Connect artifact storage, monitoring, logging and software maintenance to the fleet view.</p>
  </article>
  <article class="viona-topic">
    <h3><a href="execution.html">Workloads and execution</a></h3>
    <p>Learn how scheduling and node admission fit with Docker, Kata Containers, and Firecracker.</p>
  </article>
  <article class="viona-topic">
    <h3><a href="roadmap.html">Roadmap</a></h3>
    <p>Follow the path from architecture and a Docker prototype to an MVP and industrial pilots.</p>
  </article>
</div>
```

## Get involved

We welcome individuals and companies who want to share requirements, review the design, build integrations, or test future prototypes. Read [Contributing](contributing.md) or [open an issue](https://github.com/VIONA-project/VIONA-Platform/issues) to join the work.

Source and documentation are maintained in the [VIONA-Platform repository](https://github.com/VIONA-project/VIONA-Platform) under the [Apache License, Version 2.0](https://github.com/VIONA-project/VIONA-Platform/blob/main/LICENSE).

```{toctree}
:hidden:
:maxdepth: 2
:caption: Documentation

overview
architecture
infrastructure-lifecycle
execution
roadmap
contributing
```

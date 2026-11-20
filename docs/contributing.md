# Contributing

VIONA is being developed in the open. Individuals and companies can help define the requirements, review the architecture, and build the platform.

## Share an industrial use case

[Open an issue](https://github.com/VIONA-project/VIONA-Platform/issues) and describe:

- The industrial setting and the problem you need to solve.
- The controllers, execution environments, and hardware involved.
- The deployment, diagnostic, and recovery behavior you need.
- Any real-time, I/O, or network constraints that affect the design.

Use examples that you are allowed to share publicly.

## Review the design

Start with the [architecture](architecture.md), [workloads and execution](execution.md), and [roadmap](roadmap.md). Propose a change in an issue or a pull request, including the requirement it addresses and the tradeoffs involved.

## Improve the documentation

The documentation source is in the repository's `docs/` directory. Pages use Markdown, with MyST directives for Sphinx navigation and notices. The site uses Sphinx and the Read the Docs theme.

To build it locally with Python 3.13 or newer:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r docs/requirements.txt
python -m sphinx -b html -W --keep-going docs docs/_build/html
python -m http.server 8000 --directory docs/_build/html
```

Open `http://localhost:8000` to browse the site. Search works in the generated site without an external search service.

Before submitting a change, check the rendered page, its links, and the navigation. The documentation workflow also builds pull requests with warnings treated as errors.

## Publishing the site

Maintainers enable publishing once in the repository's **Settings → Pages** by selecting **GitHub Actions** as the source. Then run the **Documentation** workflow from the Actions tab. Subsequent changes to the documentation on `main` rebuild and publish the site automatically.

Until Pages is enabled, the workflow builds and uploads the site as an artifact and skips deployment.

## License

The project is licensed under the [Apache License, Version 2.0](https://github.com/VIONA-project/VIONA-Platform/blob/main/LICENSE). Third-party components retain their own licenses.

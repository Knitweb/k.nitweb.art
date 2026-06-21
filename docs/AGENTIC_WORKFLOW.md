# Agentic Engineering Workflow

k.nitweb.art promotes a practical AI engineering workflow for the Knitweb stack.

The reference inspiration is Kun Chen's "A Complete Walkthrough of My Agentic
Engineering Workflow", but this document translates the pattern into Knitweb
terms instead of copying one person's toolchain.

## Operating Model

| Layer | Knitweb interpretation |
| --- | --- |
| Terminal-first work | Keep build, test, review, and deployment commands reproducible across machines. |
| Memory files | Store repo layout, test commands, contracts, and prior decisions close to the code. |
| Skills | Keep conditional agent instructions small and load them only when needed. |
| Worktrees | Run parallel agents without colliding in one dirty checkout. |
| Visual evidence | Require screenshots, rendered docs, logs, or API traces for user-facing changes. |
| No-mistakes pipeline | Branch, isolated worktree, adversarial review, tests, docs, PR, CI, merge. |
| First-mate orchestration | One coordinating agent delegates small PR-sized tasks across repositories. |

## Repository Roles

| Repository | Workflow job |
| --- | --- |
| `gither` | Multi-repo navigator, dependency graph, issue-to-task planner, safe edit zones, context packs. |
| `pulse` | Protocol core, canonical bytes, gateway contracts, Lens/RLM boundaries, PoUW and ledger proofs. |
| `molgang` | Product/testbed, browser dapp, multiplayer flows, Playwright evidence, wallet/PLS economy. |
| `monitor` | Observability, node health, session timelines, quorum/relay status, public dashboards. |
| `lens` | Interpretability over fabric data, graph-to-summary, provenance explanation, anomaly reporting. |
| `news` | Public progress feed from merged PRs, woven graph events, release notes, sprint digests. |
| `k.nitweb.art` | Public gallery for the workflow, architecture, demos, and repo map. |

## Feature Loop

Every feature should move through the same loop:

1. Issue with owner repository and interface boundaries.
2. Small plan or `plan.md` when the task crosses modules.
3. Fresh worktree.
4. Reproduce bug or define acceptance test.
5. Patch.
6. Lint, unit tests, integration tests, and visual evidence where relevant.
7. Docs or public artifact update.
8. PR with test proof.
9. CI review and merge.
10. Public status update through docs/news/site.

## Agent Profile

Recommended agent defaults for Knitweb work:

- Never add agent names as commit co-authors.
- Do not manually edit generated changelogs.
- Prefer quality, correctness, robustness, scalability, and maintainability over short-term development cost.
- Start bug fixes with the closest end-user reproduction possible.
- Treat UI evidence seriously: screenshots, layout, overlap, and rendering defects matter.
- Treat lint, test failures, and flakiness as real work, even when found adjacent to the task.
- Use isolated worktrees for parallel agents.
- Keep public claims honest: hosted relays are distribution or bootstrap surfaces, not protocol trust roots.

## Public Routes

- Workflow gallery: `https://knitweb.art/` or `https://knitweb.github.io/k.nitweb.art/`
- Knitweb whitepaper: `https://knitweb.github.io/`
- Dev workflow route: `https://5mart.ml/knitweb/dev`

The `knitweb.dev` label should point to the dev workflow route until a dedicated
domain is configured.

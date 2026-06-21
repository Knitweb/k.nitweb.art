# Repository Graph

k.nitweb.art exists to make the Knitweb ecosystem legible.

The project should promote the neighboring repositories without blurring their
responsibilities. The art is the composition.

## Public Roles

| Repository | Public role | What it should prove |
| --- | --- | --- |
| `Knitweb/pulse` | Protocol fabric | Signed state, fabric proofs, gateway contracts, Lens/read-model boundaries |
| `Knitweb/molgang` | Playable dapp | Useful work, wallets, PLS/silk economy, peer updates, certificates |
| `Knitweb/knitweb` | Public gateway | Concepts, entry docs, hosted reference artifacts |
| `Knitweb/k.nitweb.art` | Integration gallery | Portable-client story, Nit reference, serverless dapp model |
| `gither` | Workflow navigator | Multi-repo graph, safe edit zones, context packs, PR impact planning |
| `monitor` | Observability | Node status, relay health, sessions, quorum, public evidence |
| `lens` | Interpretation | Provenance explanations, Lens/RLM contracts, anomaly summaries |
| `news` | Public progress | Release notes, sprint digests, woven public status |

## Linking Rule

Every public experiment should make clear which layer owns truth:

- Pulse owns protocol correctness.
- Molgang proves the protocol in an actual app loop.
- k.nitweb.art explains why portable clients matter.
- Hosted pages are distribution surfaces, not trust roots.

## Promotion Rule

k.nitweb.art should link outward to the real source repositories instead of
copying their implementation details. It can summarize, route, and frame, but
it should not become a stale mirror.

## Workflow Rule

The public workflow is:

`issue -> plan -> worktree -> tests -> visual evidence -> docs -> PR -> CI -> merge -> public update`.

`k.nitweb.art` should point people to the loop, while `knitweb.github.io` and
the `knitweb.dev` route should make the workflow visible from the public
whitepaper and developer surfaces.

## Nit Reference Placement

Nit belongs in this graph as a reference language and client-architecture
inspiration. It does not become a core dependency unless a future proof of
concept demonstrates value beyond the existing web/Python/PHP shells.

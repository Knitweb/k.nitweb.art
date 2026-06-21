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

## Nit Reference Placement

Nit belongs in this graph as a reference language and client-architecture
inspiration. It does not become a core dependency unless a future proof of
concept demonstrates value beyond the existing web/Python/PHP shells.

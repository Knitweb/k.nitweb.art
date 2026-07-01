# Worlds Narrow Web — Architecture Reference

The Worlds Narrow Web (WNW) is the settlement and governance layer beneath the
knitweb knowledge fabric.

**Core principle:** one vote per registered person per world. No operator can
mint governance weight out of thin air.

---

## 5-Seam Architecture

The WNW is a seam-based architecture: the analytics (float) world and the
knitweb (integer) world are separated by five explicit crossing points.

| # | Seam | Direction | Owner | Crossing rule |
|---|------|-----------|-------|---------------|
| 1 | **Registry (identity)** | knitweb → analytics | knitweb | Subject digest only — raw PII never stored. Two registration paths: `NATIONAL` (registry id) and `FREEPORT` (IMEI + email, for the unbanked/stateless). |
| 2 | **Marks ingest** | knitweb → analytics | both | Integer marks emitted by spiders become float analytics at an explicit divisor. The int/float boundary is declared, not implicit. |
| 3 | **World binding (WorldDAO)** | analytics ⇄ knitweb | Vank analytics | `cap()` reads the knitweb registry for `registered_persons + expected_births`. The analytics WorldDAO can only read, never write, the registry. |
| 4 | **Settlement order** | analytics → knitweb | knitweb | The float→integer crossing happens off the knitweb value-path. `SettlementOrder.amount` is a non-negative integer base unit; the knitweb module never imports the float analytics layer. |
| 5 | **Dual-signed Knit** | knitweb internal | knitweb | A `transfer_to` call on an `AccountNode` produces a signed `Knit` record with network id, nonce, and balance guards enforced. |

**Invariant:** floats never reach canonical encoding; integers never carry
analytic precision back out across a seam.

---

## Settlement kinds

| Kind | Description |
|------|-------------|
| `COUPON` | Periodic coupon payment denominated in native PLS. |
| `REDEMPTION` | Face value repayment at maturity, denominated in native PLS. |
| `CONVERSION` | Maturity taken as underlying-token units rather than PLS. |

---

## World demographic registry

Each world registered in the WNW contributes a population-anchored vote supply:

```
max_vote_supply(world) = registered_persons(world) + expected_births(world, year)
```

The `expected_births` forward allowance lets newly registered people receive a
vote within the year without requiring a mid-year cap adjustment.

`registered_persons` counts only confirmed registrations via either path:
- **NATIONAL**: verified national-registry identity
- **FREEPORT**: IMEI + email + ad-hoc proof (for the stateless/unbanked)

Both paths count toward `max_vote_supply`. Raw PII is never stored — only
content-addressed digests (`subject` for dedup, `proof` for evidence).

---

## Gateway API (knitweb.gateway)

When you run a local knitweb gateway (`knitweb.gateway.serve(app)`), the WNW
routes are available:

### `GET /api/worlds`

Returns the world demographic registry:

```json
{
  "worlds": [
    {
      "id": "earth",
      "name": "Earth",
      "registered": 8100000000,
      "expected_births": 140000000,
      "max_vote_supply": 8240000000,
      "issued": 0
    }
  ]
}
```

### `GET /api/quantum/frontier`

Returns the current best quantum circuit submission(s) stored in the App Web.
Falls back to the known ecdsafail local frontier when no signed submissions exist:

```json
{
  "frontier": [
    {"label": "Circuit", "value": "secp256k1-point-add"},
    {"label": "Score", "value": "1,582,755,898"},
    {"label": "Toffoli", "value": "1,365,622"},
    {"label": "Qubits", "value": "1159"},
    {"label": "Commit", "value": "4a90d04"},
    {"label": "Harness", "value": "ecdsafail-2026-06-21"}
  ]
}
```

### `POST /api/govern/settle`

Preview a settlement order (integer validation, no Knit executed):

Request:
```json
{"kind": "COUPON", "amount": 1000, "symbol": "PLS", "beat": 5, "world": "earth"}
```

Response (200):
```json
{
  "kind": "settlement-order",
  "settlement_kind": "COUPON",
  "amount": 1000,
  "symbol": "PLS",
  "beat": 5,
  "world": "earth",
  "_preview": true
}
```

`amount` must be a positive integer. A float amount returns `400` — the
float→integer crossing must happen before calling this endpoint.

---

## Quantum frontier — circuit challenges

Quantum circuit submissions are signed and woven into the knitweb Web as
content-addressed `quantum-circuit-submission` records. The same fabric the
WNW governance layer reads for world population is also used for circuit frontiers.

### Supported circuits

| Circuit type | Challenge | Repo |
|---|---|---|
| `secp256k1-point-add` | Reversible EC point addition | [febuz/ecdsafail](https://github.com/febuz/ecdsafail) |
| `sha256-compression` | Reversible SHA-256 compression | [sha256.fail](https://sha256.fail/) |

### Score encoding (integer-only)

Scores must be integers on the canonical path:

```
toffoli_milli = int(avg_toffoli × 1000)     # no floats
peak_qubits   = integer
score_approx  = toffoli_milli × peak_qubits // 1000
```

A challenger beats an incumbent iff:
```
challenger.toffoli_milli × challenger.peak_qubits
  < incumbent.toffoli_milli × incumbent.peak_qubits
```

This comparison is exact on milli-units — no floating-point rounding.

### Current frontier (ecdsafail, 2026-06-21)

| Metric | Value |
|---|---|
| Circuit | secp256k1-point-add |
| Score | 1,582,755,898 |
| Toffoli (avg) | 1,365,622 |
| Peak qubits | 1,159 |
| vs. baseline (10.7B) | 6.8× better |
| Commit | `4a90d04` |

---

## Quantum Weft — spherical addressing model

The WNW page now treats the future quantum/circuit surface as a **Quantum Weft**:
a spherical, layered fabric rather than a square linear construct. The working
address shape is:

```
weft_address = {
  layer: integer,      # radial shell
  theta: integer,      # angular sector, 0..359
  phi: integer,        # elevation sector, 0..179
  beat: integer,       # Pulse event time
  band: string,        # frequency / transport band
  relation: digest     # bonded neighbor, fact edge, or circuit edge
}
```

The reason to keep the address radial/angular is practical, not decorative:

- it gives humans a 360-degree AR/VR traversal surface;
- it keeps later molecule/quantum-dot addressing compatible with a visible map;
- it avoids hard-coding a square grid into a protocol that may eventually need
  optically addressable molecules, bonded molecule structures, or quantum dots;
- it maps cleanly to Pulse as the vessel that carries events within a layer and
  across layers.

### Layer stack

| Layer | Name | Function |
|---|---|---|
| 0 | Pulse vessel | Clock, event root, beat envelope, and cross-layer event timing. |
| 1 | Quantum-dot anchor | Optical or indirect address surface: laser path, dot/molecule identity, and emission band. |
| 2 | Bonded molecule ring | Element addresses bind through molecular bonds and neighbor digests. |
| 3 | Frequency shell | Outer layers may use different bands while keeping relation to the center. |
| 4 | Narrow-web fabric | P2P fact proposals, RAG slices, and LLM context packets traverse the sphere. |
| 5 | Human lens | AR/VR inspection, 360-degree movement, and detail cards. |

This is a research positioning layer today. The current implementation is a
browser-visible 2D canvas demo and deterministic address schema. It does not
claim production molecule-level hardware control.

---

## Quantum Forge — GitHub plus MLflow for circuit work

At one end of the WNW spectrum, Gither can become a shared forge for quantum
circuit code. The shape is GitHub-like for collaboration and MLflow-like for
experiment lineage, but the authority is signed records in the knitweb fabric:

- repositories hold circuit source, reversible arithmetic libraries, manifests,
  reviews, issues, and signed refs;
- run records hold backend, parameters, shots, seed, transpiler version,
  calibration hash, queue time, result CID, and integer score;
- benchmark frontiers are updated by reproducible signed runs, not by screenshots
  or one-off claims;
- review gates can require both code review and reproduction before a frontier
  claim is accepted.

Example record:

```
quantum_run = {
  repo: "Knitweb/quantum-weft",
  circuit_cid: digest,
  language: "qasm|qir|qiskit|cirq|pennylane",
  backend: "simulator|ibm|dwave|gpu|tpu",
  shots: integer,
  params_cid: digest,
  result_cid: digest,
  score_int: integer,
  review_sig: signature
}
```

This preserves the existing ecosystem split: **Gither = code forge/review**,
**Knitweb = relation fabric**, **Pulse = realtime event/activity**, and **WNW =
world/query/settlement surface**.

---

## Vank Mesh Exchange — non-custodial P2P market layer

At the other end of the spectrum, Vank can provide the market/exchange side:
a familiar Bitcoin.de/Intersango/Mt. Gox-era market experience, but without
the dangerous part: no central exchange wallet and no hosted orderbook as the
trust root.

The exchange publishes and gossips signed market facts. Users keep keys and
settlement authority client-side.

| Component | Responsibility | Must not do |
|---|---|---|
| Order intent | Signed maker/taker terms, pair, amount, price tick, expiry, jurisdiction hints. | Custody funds. |
| Gossip orderbook | Merge fresh signed offers from peers and narrow-web relays. | Become canonical truth by server position. |
| Escrow term | HTLC, multisig, bonded mediator, proof-of-payment, or local rail condition. | Hide settlement rules off-record. |
| Pulse settlement | Record opened, locked, paid, released, disputed, resolved. | Accept floats on canonical value path. |
| Reputation | Signed completion/dispute summaries and bounded exposure history. | Turn into unbounded identity scoring without proof. |

Example record:

```
vank_order = {
  pair: "BTC/EUR",
  side: "buy|sell",
  amount_int: integer,
  price_tick: integer,
  expiry_beat: integer,
  escrow: "htlc|multisig|mediator|payment-proof",
  proof_cid: digest,
  signatures: [signature]
}
```

Design rule: the product may borrow early-exchange familiarity, but it must
never recreate Mt. Gox-style custody concentration. The exchange is a P2P
coordination layer and settlement-proof fabric, not a bank.

---

## Specify, do not search

WNW's query surface is deliberately framed as **specification** rather than
search. The first interaction should return a proposal, not a full scrape:

1. classify the natural-language terms;
2. choose a fact-table shape;
3. estimate rows, columns, bytes, and relay packets;
4. show initial entities and proposed columns;
5. let the user accept, narrow, or widen scope;
6. fetch complete table rows only after acceptance.

Example: `all steel mines with detail cards in the world` maps to a proposed
mine-detail fact table before any full retrieval:

| Field | Example estimate |
|---|---|
| Rows | 9,840 |
| Columns | 18 |
| Payload | 4.6 MB |
| Relay packets | 33k x 140-character packets |
| Initial entities | Carajas Serra Norte, Kiruna, Pilbara iron ore system, Sishen |

For P2P-connected LLM use, this gives the model bounded fact slices with
provenance and byte estimates instead of a vague open-web prompt. The narrow web
is queried first because it contains organized facts. Google/LLM fallback is
reserved for under-specified questions or fields not covered by known peers.

---

## Small-device relay

The small-device path is BC2-style: a proposal can be compressed into two short
lines and carried by bitchat-like text relay. The capsule should carry only
scope, estimate, beat, and content-address hints. The full fact table is fetched
only after the peer accepts the proposed slice.

Example capsule:

```
WNW1 steel-mines rows=9840 cols=18 bytes=4.6MB beat=0
CID? est=<digest> scope=world accept=narrow/refine/query
```

Security stance: this is a field relay and proposal format, not private-key
storage. Keep the BC2 rule from the existing relay work: each message gets a
fresh message wallet when secrecy is needed.

---

## Proposed backlog

| Priority | Item | Definition of done |
|---|---|---|
| P0 | Specify contract | Signed proposal record with terms, scope, columns, row estimate, byte budget, source layer, and accept/refine decision. |
| P0 | Fact table planner | Deterministic estimate-before-fetch planner with cached estimates per Pulse beat. |
| P1 | BC2 adapter | Two-line proposal capsules for bitchat-style field relay. |
| P1 | Quantum Weft schema | Canonical radial/angular address type with layer, theta, phi, beat, band, and relation digest. |
| P1 | AR/VR fabric view | WebXR demo that inspects shells, traverses 360 degrees, and opens detail cards. |
| P2 | Quantum circuit bridge | Circuit submissions mapped into weft coordinates and compared as signed QPU/GPU/TPU records. |
| P2 | Quantum Forge runs | MLflow-like run records for circuit code: params, backend, shots, result CID, score, and review signature. |
| P2 | Vank mesh orderbook | Non-custodial signed order intents, gossip merge rules, expiry, escrow terms, and settlement proof states. |
| P2 | P2P RAG slices | Bounded fact slices attached to LLM context with provenance and byte estimates. |
| P3 | Molecule addressing research | Track laser, quantum-dot, and optically addressable molecular-qubit work without claiming hardware readiness too early. |
| P3 | Post-2036 digital twin | Keep today's protocol digitally prepared for future molecule fabrics while shipping useful web facts now. |

---

## Research anchors

The linked ScienceDirect page (`S002223131100723X`) is treated as user-provided
spherical positioning. The local fetch did not expose article metadata, so the
title is not restated here.

Usable anchors for the current WNW story:

- Nobel Prize in Chemistry 2023 press release:
  <https://www.nobelprize.org/prizes/chemistry/2023/press-release/>
  - quantum dots are real size-dependent quantum systems and are a useful
    public reference for explaining why dot size/frequency matters.
- RFC 9340, *Architectural Principles for a Quantum Internet*:
  <https://www.rfc-editor.org/rfc/rfc9340>
  - quantum networks remain hybrid classical-quantum systems; WNW can act as
    the deterministic classical control/fact layer.
- Bayliss et al., *Enhancing Spin Coherence in Optically Addressable Molecular
  Qubits through Host-Matrix Control*:
  <https://arxiv.org/abs/2204.00168>
  - optically addressable molecular spins support the longer-term molecule
    addressing research direction.
- Journal of Luminescence examples on spherical quantum-dot systems, for
  example DOI `10.1016/j.jlumin.2022.119181`, support keeping spherical
  quantum-dot models visible in the research track.

---

## Implementation references

| Component | Location |
|---|---|
| WorldRegistry | `pulse/src/knitweb/govern/worlds.py` |
| SettlementOrder / settle_preview | `pulse/src/knitweb/govern/settle.py` |
| QuantumKnitweb | `pulse/src/knitweb/knitwebs/quantum/__init__.py` |
| Gateway WNW routes | `pulse/src/knitweb/gateway.py` (`_quantum_frontier_stats`, `_parse_settle_body`, `/api/*`) |
| Vank analytics (float side) | `vank/src/knitweb_vank/settle.py` |
| Vank demographics | `vank/src/knitweb_vank/registry.py` |
| WNW web3 page | `k.nitweb.art/worlds.html` |
| Quantum Weft page demo | `k.nitweb.art/worlds.html#quantum-weft` |
| Quantum Forge + Vank exchange spectrum | `k.nitweb.art/worlds.html#spectrum` |
| Specify interface | `k.nitweb.art/worlds.html#specify` |
| PDF backlog | `k.nitweb.art/output/pdf/wnw-quantum-weft-backlog.pdf` |

---

## Serverless dapp model

The WNW web3 page (`worlds.html`) follows the serverless dapp model:

- **Client holds keys.** The wallet address is derived in the browser and stored
  in `localStorage`. No key material leaves the device.
- **Protocol owns state.** World counts, settlement orders, and circuit scores
  are signed records in the knitweb fabric — not rows in an app server's database.
- **Transport is replaceable.** The gateway URL is configurable; the page falls
  back to demo data when no gateway is reachable.
- **Float analytics never touches canonical encoding.** Settlement amounts arrive
  as integers; the page sends them as integers; the gateway validates integer-only.

See [SERVERLESS_DAPP_MODEL.md](SERVERLESS_DAPP_MODEL.md) for the general model.

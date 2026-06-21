# Nit Reference

Nitweb.art uses Nit as a reference point, not as the protocol runtime.

## What Nit Shows Well

The Nit calculator example is useful because it separates:

- `calculator_logic.nit` - pure application/business logic;
- `calculator.nit` - portable app UI over `app.nit`;
- Android/iOS modules - platform refinements around the same app logic.

The project Makefile builds desktop binaries, Android APKs, and iOS app bundles
from the same application family.

For Knitweb this is the important lesson: the client shell can change without
rewriting the state model.

## What We Do Not Claim

Nit does not make an application serverless or peer-to-peer by itself. The
serverless property must come from:

- local key ownership;
- signed state transitions;
- verifiable storage/proofs;
- replaceable transport;
- explicit relay selection instead of hard-coded central hosts.

That role belongs to Knitweb/Pulse.

## Why It Helps k.nitweb.ai

Nit is a stable, lesser-known language ecosystem. Referencing it helps signal
that Knitweb is not just a web framework or Python package. It is a fabric that
can be rendered by unusual, durable, and native-feeling clients.

## Possible Proof Of Concept

A small Nit-inspired proof should avoid blockchain theater and focus on a real
portable-client contract:

1. Load a signed Knitweb state fixture.
2. Render wallet identity, useful work, and relation graph.
3. Sign one local intent.
4. Export the intent as protocol JSON.
5. Submit it through an explicit peer/relay endpoint.

Only step 5 should care about transport.

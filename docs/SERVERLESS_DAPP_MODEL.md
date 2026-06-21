# Serverless Dapp Model

Nitweb.art frames the ideal k.nitweb.ai dapp as a protocol-owned application,
not a server-owned website.

## Principle

The server may deliver files or relay messages, but it must not own user truth.

The core user truth is:

- wallet identity;
- signed intents;
- useful-work records;
- proof links;
- portable read models.

## Layers

| Layer | Responsibility | Must Not Do |
| --- | --- | --- |
| Client shell | Render state, collect user intent, hold local keys | Become the source of truth |
| Knitweb/Pulse core | Verify signatures, proofs, relations, and useful work | Hide authority in one hosted app |
| Transport | Relay, sync, or gossip messages | Require one permanent central endpoint |
| Storage | Persist snapshots, proofs, and fabric state | Store private wallet control material |

## Android Dapp Shape

An Android dapp should be a shell around the same signed protocol state as the
web client:

1. Local wallet secret is created or recovered on-device.
2. The UI renders a canonical read model.
3. User actions become signed intents.
4. Intents are sent through a configured peer/relay.
5. The client can switch relay without changing wallet identity.

This is where the Nit calculator pattern is relevant: keep logic portable and
refine platform interaction around it.

## What Comes Next

The next useful repository milestones are:

- define a tiny signed-state fixture in `fixtures/`;
- publish a browser renderer for that fixture;
- add an Android-client design note;
- create a first transport-neutral intent format;
- later, experiment with Nit or Nit-inspired native-client code.

# k.nitweb.art

k.nitweb.art is a small public artifact for the Knitweb ecosystem: a place to
explain portable, native-feeling dapps built around a serverless peer-to-peer
protocol core.

The `k.` prefix makes the intent explicit: this is Knitweb's art surface, not a
standalone Nit-language fork.

The name still references two ideas:

- **Nit** as a stable, lesser-known language with a useful portable-app pattern:
  keep logic in one core and refine the shell per platform.
- **Knitweb** as the protocol/fabric layer where identity, useful work, and
  state proofs belong.

This repository is intentionally static-first. The first version is a GitHub
Pages-ready site with no build step.

## Why This Exists

Knitweb apps should not depend on one central server owning account state. The
ideal client shape is:

1. A portable signed-state core.
2. Thin platform shells for web, Android, desktop, or experimental languages.
3. P2P or relay-assisted transport that can be replaced without changing wallet
   or proof semantics.

Nit's calculator example is a useful reference for the first two points: it
keeps calculator logic separate from the platform UI, then refines Android and
iOS behavior around the same logic.

## Repository Layout

- `index.html` - static public site.
- `styles.css` - site styling.
- `docs/REPOSITORY_GRAPH.md` - how the Knitweb repositories promote and depend
  on each other.
- `docs/NIT_REFERENCE.md` - what we borrow from Nit and what we do not.
- `docs/SERVERLESS_DAPP_MODEL.md` - ideal dapp architecture for k.nitweb.ai.

## Current Scope

This is not a production Nit runtime integration yet. It is a positioning and
design artifact for k.nitweb.ai, Molgang, and Pulse:

- promote the active Knitweb repositories as one coherent protocol/app stack;
- use Nit as an external reference for portable client architecture;
- keep Pulse/Knitweb as the protocol source of truth;
- avoid presenting a hosted PHP/Python server as the product's trust root.

## Local Preview

Open `index.html` directly in a browser, or run:

```bash
python3 -m http.server 8769
```

Then visit `http://127.0.0.1:8769/`.

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_homepage_links_core_docs() -> None:
    html = read("index.html")

    assert 'href="docs/SERVERLESS_DAPP_MODEL.md"' in html
    assert 'href="docs/NIT_REFERENCE.md"' in html
    assert 'href="docs/REPOSITORY_GRAPH.md"' in html
    assert 'href="docs/AGENTIC_WORKFLOW.md"' in html
    assert "k.nitweb.art" in html


def test_homepage_promotes_core_repositories() -> None:
    html = read("index.html")

    for repo in (
        "https://github.com/Knitweb/pulse",
        "https://github.com/Knitweb/molgang",
        "https://github.com/Knitweb/knitweb.github.io",
        "https://github.com/Knitweb/k.nitweb.art",
        "https://knitweb.github.io/professions/",
    ):
        assert repo in html


def test_nit_reference_keeps_protocol_claims_honest() -> None:
    doc = read("docs/NIT_REFERENCE.md")

    assert "Nit does not make an application serverless or peer-to-peer by itself" in doc
    assert "That role belongs to Knitweb/Pulse" in doc


def test_serverless_model_rejects_server_owned_truth() -> None:
    doc = read("docs/SERVERLESS_DAPP_MODEL.md")

    assert "The server may deliver files or relay messages, but it must not own user truth" in doc
    assert "Store private wallet control material" in doc


def test_agentic_workflow_promotes_repo_loop_and_dev_route() -> None:
    doc = read("docs/AGENTIC_WORKFLOW.md")

    assert "`gither`" in doc
    assert "`pulse`" in doc
    assert "`molgang`" in doc
    assert "Fresh worktree" in doc
    assert "https://knitweb.art/" in doc
    assert "https://5mart.ml/knitweb/dev" in doc


def test_custom_domain_is_knitweb_art() -> None:
    assert read("CNAME").strip() == "knitweb.art"

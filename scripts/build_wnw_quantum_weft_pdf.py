from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "wnw-quantum-weft-backlog.pdf"


def styles():
    base = getSampleStyleSheet()
    base["Title"].fontName = "Helvetica-Bold"
    base["Title"].fontSize = 24
    base["Title"].leading = 29
    base["Title"].textColor = colors.HexColor("#eef4f8")
    base["Title"].alignment = TA_CENTER
    base["Heading1"].fontName = "Helvetica-Bold"
    base["Heading1"].fontSize = 16
    base["Heading1"].leading = 20
    base["Heading1"].spaceBefore = 16
    base["Heading1"].spaceAfter = 8
    base["Heading1"].textColor = colors.HexColor("#10161b")
    base["Heading2"].fontName = "Helvetica-Bold"
    base["Heading2"].fontSize = 12
    base["Heading2"].leading = 15
    base["Heading2"].spaceBefore = 10
    base["Heading2"].spaceAfter = 5
    base["BodyText"].fontName = "Helvetica"
    base["BodyText"].fontSize = 9.5
    base["BodyText"].leading = 13.2
    base["BodyText"].spaceAfter = 7
    base["BodyText"].textColor = colors.HexColor("#202830")
    base.add(
        ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontSize=8,
            leading=10.5,
            textColor=colors.HexColor("#4a5964"),
        )
    )
    base.add(
        ParagraphStyle(
            "TableHead",
            parent=base["Small"],
            fontName="Helvetica-Bold",
            textColor=colors.white,
        )
    )
    base.add(
        ParagraphStyle(
            "CoverSub",
            parent=base["BodyText"],
            fontSize=11,
            leading=15,
            textColor=colors.HexColor("#d7e6ee"),
            alignment=TA_CENTER,
        )
    )
    return base


def p(text, style="BodyText"):
    return Paragraph(text, S[style])


def bullets(items):
    return ListFlowable(
        [ListItem(p(item), leftIndent=4) for item in items],
        bulletType="bullet",
        leftIndent=14,
        bulletFontName="Helvetica",
        bulletFontSize=7,
    )


def table(rows, widths=None):
    data = []
    for row_i, row in enumerate(rows):
        style = "TableHead" if row_i == 0 else "Small"
        data.append([p(str(cell), style) for cell in row])
    t = Table(data, colWidths=widths, hAlign="LEFT", repeatRows=1)
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#10161b")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#b9c5cc")),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f8fbfc")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return t


def page(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(colors.HexColor("#4a5964"))
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(18 * mm, 10 * mm, "WNW Quantum Weft - research and backlog")
    canvas.drawRightString(192 * mm, 10 * mm, str(doc.page))
    canvas.restoreState()


S = styles()
story = []

cover = Table(
    [
        [p("WNW Quantum Weft", "Title")],
        [
            p(
                "Spherical narrow-web layers for estimate-first facts, small-device relay, "
                "P2P RAG slices, and future quantum circuit development.",
                "CoverSub",
            )
        ],
    ],
    colWidths=[170 * mm],
    rowHeights=[34 * mm, 38 * mm],
)
cover.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#0b0d10")),
            ("BOX", (0, 0), (-1, -1), 1.2, colors.HexColor("#5fd0a5")),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("LEFTPADDING", (0, 0), (-1, -1), 18),
            ("RIGHTPADDING", (0, 0), (-1, -1), 18),
        ]
    )
)
story += [Spacer(1, 30 * mm), cover, Spacer(1, 18 * mm)]
story.append(
    p(
        "Positioning date: 2026-06-30. The ScienceDirect PII page supplied with the request "
        "was reachable only as a generic ScienceDirect shell in this environment, so its title "
        "is not restated. The design below uses it as directional spherical positioning and "
        "grounds claims in accessible sources listed at the end.",
        "Small",
    )
)
story.append(PageBreak())

story.append(p("1. Design Thesis", "Heading1"))
story.append(
    p(
        "WNW should become the efficient narrow-web layer between worlds and between small "
        "devices. It should not behave like a broad search engine by default. A user specifies "
        "information; WNW returns a proposal with result size and table shape before fetching "
        "complete facts.",
    )
)
story.append(
    bullets(
        [
            "Spherical fabric over square grid: use layer, theta, phi, beat, band, and relation digest.",
            "Pulse is the vessel: it carries event timing within layers and between layers.",
            "Narrow web first: organized facts beat open-web search for specified questions.",
            "LLM second: call Google or an LLM only when the request is under-specified or a field is missing.",
            "Quantum Forge: code, circuit manifests, and MLflow-like run records share the same signed fabric.",
            "Vank Mesh Exchange: market UX without exchange custody or a central orderbook trust root.",
            "Always visual: every architecture surface needs a traversable AR/VR-ready demo.",
        ]
    )
)

story.append(p("2. Quantum Weft Layers", "Heading1"))
story.append(
    table(
        [
            ["Layer", "Name", "Function"],
            ["0", "Pulse vessel", "Clock, event root, beat envelope, and cross-layer event timing."],
            ["1", "Quantum-dot anchor", "Optical or indirect address surface: laser path, dot/molecule identity, emission band."],
            ["2", "Bonded molecule ring", "Element addresses bind through molecular bonds and neighbor digests."],
            ["3", "Frequency shell", "Outer layers may use different bands while staying connected to the center."],
            ["4", "Narrow-web fabric", "P2P fact proposals, RAG slices, and LLM context packets traverse the sphere."],
            ["5", "Human lens", "AR/VR inspection, 360-degree movement, and detail cards."],
        ],
        [16 * mm, 42 * mm, 104 * mm],
    )
)
story.append(
    p(
        "The hardware-facing claim is deliberately conservative: WNW is digitally prepared for "
        "future optically addressable molecules or quantum-dot mediated addressing, but today it "
        "ships a deterministic schema and browser demo, not a molecule-control product.",
    )
)

story.append(PageBreak())
story.append(p("3. Quantum Forge", "Heading1"))
story.append(
    p(
        "At one end of the WNW spectrum, Gither becomes a shared forge for "
        "quantum circuit code. It should feel GitHub-like for collaboration "
        "and MLflow-like for experiment lineage, while signed records in the "
        "fabric remain the authority."
    )
)
story.append(
    table(
        [
            ["Surface", "Record", "Purpose"],
            ["Circuit repo", "QASM, QIR, Qiskit, Cirq, PennyLane, reversible libraries", "Code, issues, reviews, signed refs, and merge gates."],
            ["Experiment run", "backend, shots, seed, transpiler, calibration hash, queue time, result CID", "Run lineage without one MLflow server owning truth."],
            ["Benchmark frontier", "Toffoli, depth, qubits, fidelity, cost, integer score", "Reproducible comparison before accepting a claimed improvement."],
        ],
        [34 * mm, 66 * mm, 60 * mm],
    )
)
story.append(
    p(
        "Example record: quantum_run = {repo, circuit_cid, language, backend, "
        "shots, params_cid, result_cid, score_int, review_sig}.",
        "Small",
    )
)

story.append(p("4. Vank Mesh Exchange", "Heading1"))
story.append(
    p(
        "At the other end of the spectrum, Vank provides a non-custodial P2P "
        "market layer. It may borrow familiarity from Bitcoin.de, Intersango, "
        "and Mt. Gox-era exchange UX, but it must not recreate their custody "
        "concentration. Users keep keys; the fabric gossips signed market facts."
    )
)
story.append(
    table(
        [
            ["Component", "Responsibility", "Must not do"],
            ["Order intent", "Signed pair, side, amount, price tick, expiry, jurisdiction hints.", "Custody funds."],
            ["Gossip orderbook", "Merge fresh signed offers from peers and narrow-web relays.", "Become canonical truth by server position."],
            ["Escrow term", "HTLC, multisig, bonded mediator, payment proof, or local rail condition.", "Hide settlement rules off-record."],
            ["Pulse settlement", "Record opened, locked, paid, released, disputed, resolved.", "Accept floats on canonical value path."],
        ],
        [34 * mm, 72 * mm, 54 * mm],
    )
)
story.append(
    p(
        "Example record: vank_order = {pair, side, amount_int, price_tick, "
        "expiry_beat, escrow, proof_cid, signatures}.",
        "Small",
    )
)

story.append(PageBreak())
story.append(p("5. Specify Flow", "Heading1"))
story.append(
    p(
        "The initial scan returns the proposed fact table before the expensive retrieval. "
        "For the example 'all steel mines with detail cards in the world', WNW proposes rows, "
        "columns, payload size, and initial entities."
    )
)
story.append(
    table(
        [
            ["Field", "Example estimate"],
            ["Rows", "9,840"],
            ["Columns", "18"],
            ["Payload", "4.6 MB"],
            ["Relay packets", "About 33k x 140-character packets"],
            ["Initial entities", "Carajas Serra Norte, Kiruna, Pilbara iron ore system, Sishen"],
            ["Decision", "Accept, narrow scope, or widen to public web fallback"],
        ],
        [45 * mm, 115 * mm],
    )
)
story.append(p("The proposal record should contain:", "Heading2"))
story.append(
    bullets(
        [
            "terms and normalized domain",
            "source scope: nearby, known peers, world, or fallback web",
            "columns and expected row count",
            "estimated byte payload and small-device packet count",
            "initial entity list and unresolved fields",
            "provenance confidence and Pulse beat",
        ]
    )
)

story.append(p("6. Small-Device Relay", "Heading1"))
story.append(
    p(
        "For bitchat-like communication, WNW should send the proposal, not the whole table. "
        "A BC2-style capsule can carry scope, estimates, beat, and content-address hints in "
        "two short lines. The full slice is fetched only after acceptance."
    )
)
story.append(
    table(
        [
            ["Line", "Example"],
            ["1", "WNW1 steel-mines rows=9840 cols=18 bytes=4.6MB beat=0"],
            ["2", "CID? est=&lt;digest&gt; scope=world accept=narrow/refine/query"],
        ],
        [18 * mm, 142 * mm],
    )
)
story.append(
    p(
        "Security stance: this is field relay and proposal transport, not private-key storage. "
        "When secrecy is needed, keep the BC2 convention that each message gets a fresh message wallet.",
    )
)

story.append(PageBreak())
story.append(p("7. Proposed Backlog", "Heading1"))
story.append(
    table(
        [
            ["Priority", "Item", "Definition of done"],
            ["P0", "Specify contract", "Signed proposal record with terms, scope, columns, estimates, source layer, and accept/refine decision."],
            ["P0", "Fact table planner", "Deterministic estimate-before-fetch planner with cached estimates per Pulse beat."],
            ["P1", "BC2 adapter", "Two-line proposal capsules for bitchat-style field relay."],
            ["P1", "Quantum Weft schema", "Canonical radial/angular address type with layer, theta, phi, beat, band, and relation digest."],
            ["P1", "AR/VR fabric view", "WebXR demo that inspects shells, traverses 360 degrees, and opens detail cards."],
            ["P2", "Quantum circuit bridge", "Circuit submissions mapped into weft coordinates and compared as signed QPU/GPU/TPU records."],
            ["P2", "Quantum Forge runs", "MLflow-like run records for circuit code: params, backend, shots, result CID, score, and review signature."],
            ["P2", "Vank mesh orderbook", "Non-custodial signed order intents, gossip merge rules, expiry, escrow terms, and settlement proof states."],
            ["P2", "P2P RAG slices", "Bounded fact slices attached to LLM context with provenance and byte estimates."],
            ["P3", "Molecule addressing research", "Track laser, quantum-dot, and molecular-qubit work without claiming hardware readiness too early."],
            ["P3", "Post-2036 digital twin", "Keep today's protocol ready for future molecule fabrics while shipping useful web facts now."],
        ],
        [20 * mm, 42 * mm, 98 * mm],
    )
)

story.append(p("8. Source Anchors", "Heading1"))
story.append(
    bullets(
        [
            "User-provided ScienceDirect PII: https://www.sciencedirect.com/science/article/abs/pii/S002223131100723X. Metadata was not exposed in this environment.",
            "Nobel Prize in Chemistry 2023 press release on quantum dots: https://www.nobelprize.org/prizes/chemistry/2023/press-release/",
            "RFC 9340, Architectural Principles for a Quantum Internet: https://www.rfc-editor.org/rfc/rfc9340",
            "Bayliss et al., Enhancing Spin Coherence in Optically Addressable Molecular Qubits through Host-Matrix Control: https://arxiv.org/abs/2204.00168",
            "Journal of Luminescence spherical quantum-dot example DOI: https://doi.org/10.1016/j.jlumin.2022.119181",
        ]
    )
)

doc = SimpleDocTemplate(
    str(OUT),
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=16 * mm,
    bottomMargin=16 * mm,
)
doc.build(story, onFirstPage=page, onLaterPages=page)
print(OUT)

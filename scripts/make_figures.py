#!/usr/bin/env python3
"""Generate Figures 1-3 for the HATL/HBTL sovereignty paper (PNG + PDF)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})

C_SOV = "#dde7f5"; C_OP = "#f5ecdd"; C_SYS = "#e8e8e8"; C_TXT = "#1a1a1a"; EDGE = "#444444"

def box(ax, x, y, w, h, text, fc, fs=10, bold=False):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.02",
                              fc=fc, ec=EDGE, lw=1.2, mutation_aspect=1))
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=fs,
            color=C_TXT, fontweight="bold" if bold else "normal")

def arrow(ax, x1, y1, x2, y2, text="", dashed=False, tx=None, ty=None):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="<->", mutation_scale=14,
                               lw=1.2, color=EDGE, linestyle="--" if dashed else "-"))
    if text:
        ax.text(tx if tx is not None else (x1+x2)/2 + 0.15,
                ty if ty is not None else (y1+y2)/2,
                text, fontsize=8.5, ha="left", va="center", color=C_TXT)

# ---------------- Figure 1 ----------------
fig, ax = plt.subplots(figsize=(7.2, 4.8))
ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")

box(ax, 1.2, 8.0, 7.6, 1.7, "ABOVE — Frame Sovereignty\nreopenability: premises, objectives,\ndelegation, classification, meta-game",
    C_SOV)
ax.text(0.15, 8.85, "SOVEREIGN\nLAYER", fontsize=8, rotation=90, va="center", ha="center")

box(ax, 1.2, 4.6, 3.5, 1.5, "IN THE LOOP\napprove / reject\nper-decision", C_OP)
box(ax, 5.3, 4.6, 3.5, 1.5, "ON THE LOOP\nmonitor / intervene\ncontinuous supervision", C_OP)
box(ax, 1.2, 2.3, 7.6, 1.5, "AUTONOMOUS SYSTEM\n(perceive — decide — act)", C_SYS)
ax.text(0.15, 5.3, "OPERATIONAL\nLAYER", fontsize=8, rotation=90, va="center", ha="center")

box(ax, 1.2, 0.15, 7.6, 1.7, "BELOW — Effect Sovereignty\ninterruptibility: permissions, actuation gates,\nseparability, chokepoints, revocation",
    C_SOV)
ax.text(0.15, 1.0, "SOVEREIGN\nLAYER", fontsize=8, rotation=90, va="center", ha="center")

arrow(ax, 5.0, 8.0, 5.0, 6.15, "authority over frames", tx=5.2, ty=7.0)
arrow(ax, 5.0, 2.3, 5.0, 1.9, "authority over effects", tx=5.2, ty=2.1)

fig.suptitle("Figure 1. Two-layer architecture: operational participation within, sovereign capacities over",
             fontsize=10.5)
fig.savefig(f"{OUT}/fig1_architecture.png", dpi=300, bbox_inches="tight")
fig.savefig(f"{OUT}/fig1_architecture.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------- Figure 2 ----------------
fig, ax = plt.subplots(figsize=(7.6, 5.0))
ax.set_xlim(0, 12); ax.set_ylim(0, 12); ax.axis("off")

# decisions column (top half)
for i in range(6):
    ax.add_patch(plt.Circle((1.0, 8.0 + i*0.55), 0.15, fc="#c9d7ea", ec=EDGE, lw=0.8))
ax.text(1.0, 11.5, "decisions\n(λ → large)", fontsize=8.5, ha="center")
ax.text(3.0, 11.0, "classify", fontsize=8, style="italic")
arrow(ax, 1.45, 9.4, 3.6, 9.4)
for ty in (10.4, 9.4, 8.4):
    box(ax, 3.6, ty-0.3, 1.6, 0.62, "class", "#eee6f5", fs=9)
ax.text(4.4, 11.5, "decision classes", fontsize=8.5, ha="center")
ax.text(5.9, 11.0, "assign frame", fontsize=8, style="italic")
arrow(ax, 5.25, 9.4, 6.7, 9.4)
box(ax, 6.7, 8.7, 2.0, 1.4, "frames\n(few)", C_SOV, fs=9, bold=True)

# actions column (bottom half)
for i in range(6):
    ax.add_patch(plt.Circle((1.0, 2.2 + i*0.55), 0.15, fc="#f0d9c0", ec=EDGE, lw=0.8))
ax.text(1.0, 5.9, "actions\n(λ → large)", fontsize=8.5, ha="center")
ax.text(3.0, 5.2, "classify", fontsize=8, style="italic")
arrow(ax, 1.45, 3.6, 3.6, 3.6)
for ty in (4.6, 3.6, 2.6):
    box(ax, 3.6, ty-0.3, 1.6, 0.62, "permission\nclass", "#eee6f5", fs=8)
ax.text(5.9, 5.2, "gate", fontsize=8, style="italic")
arrow(ax, 5.25, 3.6, 6.7, 3.6)
box(ax, 6.7, 2.9, 2.0, 1.4, "effect\nboundaries\n(few)", C_SOV, fs=9, bold=True)

# HUMAN
box(ax, 9.6, 5.4, 2.0, 2.6, "HUMAN\nattention\nH < ∞", "#f5dada", fs=9, bold=True)
arrow(ax, 8.75, 9.4, 10.1, 8.05, "")
arrow(ax, 8.75, 3.6, 10.1, 5.35, "")
ax.text(10.6, 9.3, "attention spent on\nframes + boundaries\nconstrains arbitrarily\nmany decisions/actions",
        fontsize=8, ha="center")

ax.text(0.3, 0.6, "Per-decision In/On costs rise with λ; frames and boundaries compress the spaces\n"
                "that per-decision attention must cover.", fontsize=8.5, style="italic")
fig.suptitle("Figure 2. Attention-efficient sovereignty: compression of decision- and action-spaces",
             fontsize=10.5)
fig.savefig(f"{OUT}/fig2_attention.png", dpi=300, bbox_inches="tight")
fig.savefig(f"{OUT}/fig2_attention.pdf", bbox_inches="tight")
plt.close(fig)

# ---------------- Figure 3 ----------------
fig, ax = plt.subplots(figsize=(7.6, 4.8))
ax.set_xlim(0, 12); ax.set_ylim(0, 10.5); ax.axis("off")

box(ax, 0.4, 8.4, 3.0, 1.4, "novel system N\nforegrounded", "#dcecdc", fs=9)
box(ax, 0.4, 5.8, 3.0, 1.4, "legacy baseline L\nrecedes to background", "#f5ecdd", fs=9)
box(ax, 4.4, 5.8, 3.0, 1.6, "governance question:\n'integrate N into L?'\nL = L₀ fixed", C_SYS, fs=8.5)
box(ax, 8.4, 8.4, 3.5, 1.4, "effective reopenability\n$A_{eff}(t)$ decays if unmaintained", "#f5dada", fs=8)
box(ax, 8.4, 5.8, 3.5, 1.4, "effective interruptibility\n$B_{eff}(t)$ decays if unmaintained", "#f5dada", fs=8)
box(ax, 8.4, 3.0, 3.5, 1.4, "backgrounding\ndividend (hypothesis)", "#efe6c9", fs=8)
box(ax, 0.4, 0.4, 8.4, 1.5,
    "BACKGROUND-INVARIANT SOVEREIGNTY\n$A_{eff}(t)$ ≥ $A_{min}$ ,  $B_{eff}(t)$ ≥ $B_{min}$  —  dormant but callable",
    C_SOV, fs=9, bold=True)

arrow(ax, 1.9, 8.4, 1.9, 7.25, "")
arrow(ax, 3.45, 6.5, 4.35, 6.5, "")
arrow(ax, 7.45, 6.6, 8.35, 9.0, "")
arrow(ax, 7.45, 6.4, 8.35, 6.4, "")
arrow(ax, 7.45, 6.2, 8.35, 3.7, "")
# maintenance arrow up the left side of the decay column
arrow(ax, 3.9, 1.9, 5.6, 5.75, "", dashed=True)
ax.text(2.6, 3.4, "maintenance:\nreopening triggers,\nproof-of-interruption\nexercises", fontsize=8,
        ha="left", va="center")

fig.suptitle("Figure 3. Backgrounding dynamics and the two dormant-but-callable invariants",
             fontsize=10.5)
fig.savefig(f"{OUT}/fig3_backgrounding.png", dpi=300, bbox_inches="tight")
fig.savefig(f"{OUT}/fig3_backgrounding.pdf", bbox_inches="tight")
plt.close(fig)

print("done")

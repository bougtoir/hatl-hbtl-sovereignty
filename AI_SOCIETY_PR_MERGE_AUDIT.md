# AI & SOCIETY — PR Merge Audit

Date: 2026-10-15. Scope: repository state and open PRs relevant to the AI & Society
submission package for `hatl-hbtl-sovereignty/`.

## A. Current repository state

- Active branch: `devin/1791854823-hatl-hbtl-ai-society` (this PR's head), synced with origin.
- Last merged project PR: #551 (original Philosophy & Technology package) and #657
  (journal reselection). The prior project branch `devin/1790546746-hatl-hbtl-sovereignty`
  supplied the previously synced public tree.
- Working tree clean; generated artifacts committed.

## B. Relevant PR table

| PR | Title | Branch | Content | Affects manuscript | Affects package | Affects public sync | Affects private-only | Superseded | Depends on | Recommendation |
|----|-------|--------|---------|--------------------|-----------------|---------------------|----------------------|------------|------------|----------------|
| #667 | hatl-hbtl-sovereignty: AI & Society retarget — adapted manuscript + submission package | devin/1791854823-hatl-hbtl-ai-society | AI & Society-adapted manuscript, hostile-review revisions, submission package, cover letter, audit reports, handoffs, sync-map entries incl. EXCLUDE_MAP | yes | yes | yes — adds BRANCH_MAP/SUBDIR_MAP/EXCLUDE_MAP | yes — keeps private material private via EXCLUDE_MAP | no | none | MERGE NOW |

No other open PR touches this project. The older branch
`devin/1790546746-hatl-hbtl-sovereignty` has no open PR (merged via #551).

## C. PUBLIC_SYNC_GATE result

**PUBLIC_SYNC_GATE = PASS (after the EXCLUDE_MAP fix committed to PR #667).**

Prior state was FAIL: both `devin/1790546746-hatl-hbtl-sovereignty` and
`devin/1791854823-hatl-hbtl-ai-society` had BRANCH_MAP/SUBDIR_MAP entries but no
EXCLUDE_MAP entries, so pushes synced the entire subdir — including
`manuscript/*.docx`, `submission/` (cover letter, package ZIP), `audits/`,
handoffs and ledgers — to the public mirror `bougtoir/hatl-hbtl-sovereignty`.

Fix (in PR #667): EXCLUDE_MAP entries for both branches exclude
`manuscript submission audits literature tables references` plus all root-level
ledger/handoff/audit files and `scripts/build_docx.py` (the prose-bearing docx
builder). Simulated post-exclusion public tree contains only:

```
figures/fig1_architecture.{pdf,png}
figures/fig2_attention.{pdf,png}
figures/fig3_backgrounding.{pdf,png}
scripts/make_figures.py
```

This matches the approved public scope (figure-reproduction code + figures only).

Residual note: the public mirror's current `main` still carries the previously
synced full subdir from earlier pushes. The next sync run after this PR merges —
and any push-triggered run on this branch — publishes the filtered tree with
`--delete` semantics, removing the leaked paths. Verify the public tree after
merge.

## D. Exact merge order

Single PR. No ordering constraints.

## E. Final recommendation

The submission package is internally consistent; the only open PR carries both
the submission state and the sync-privacy fix required before publication.

FINAL MERGE RECOMMENDATION:
- Merge PR #667.

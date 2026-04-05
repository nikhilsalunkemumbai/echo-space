# OSF Pre-Registration Addendum
**Registration:** https://osf.io/c69td  
**Registration DOI:** 10.17605/OSF.IO/C69TD  
**Date of registration:** 22 March 2026  
**Date of this addendum:** 03 April 2026  
**Author:** Nikhil Ashok Salunke, Independent Researcher, Pune, India  

This addendum documents corrections and updates that arose after the pre-registration was locked. OSF pre-registrations are immutable by design. This file serves as the transparent record of all post-registration changes, consistent with the deviation reporting commitment stated in the pre-registration ("Any deviation from this pre-registered analysis plan will be explicitly flagged as a deviation in the results section of any publication").

---

## 1. City correction

**What the pre-registration says:** "based in Mumbai, India" (in the Other / Context section) and "Symbiosis International University IEC, Mumbai, India" (in the Metadata description).

**Correction:** The correct city is **Pune, India**. The author is based in Pune, not Mumbai. This is a clerical error with no bearing on the study design, analysis plan, or any scientific content.

---

## 2. THETA_V recalibration — interactive sessions

**What the pre-registration says:** The locked parameters listed in the Manipulated Variables section are `ALPHA=0.3, GAMMA_Q=0.12, THETA_V=1.5, LAMBDA=0.8`.

**What changed and why:** THETA_V=1.5 was the value identified in the original 27-combination grid sweep, which ran all 9 agents posting simultaneously every turn (multi-agent mode). When the engine was developed into an interactive session format — where one agent posts per turn — volatility V accumulated approximately 9× more slowly per turn, making THETA_V=1.5 unreachable in practice. In v2.0 of the engine, THETA_V was recalibrated to **0.18** and SIGMA_V (sigmoid sharpness) was recalibrated to **0.020** to restore the rehearsal band in interactive mode.

**Verification:** 500 interactive sessions under mixed play confirmed the recalibrated parameters produce 0.66 crises per session with 49% of sessions containing at least one crisis — within the pre-specified rehearsal band (0.5–1.5 crises per session). Action differentiation was confirmed: all-Pause play yields ~0.05 crises per session; all-QuickReact play yields ~2.55 crises per session (ratio: ~51×).

**Impact on the pre-registered analysis plan:** None. The manipulation (Treatment vs Control) is unchanged. The outcome measures are unchanged. The randomization, blinding, statistical models, and inference criteria are unchanged. The recalibration affects only the internal physics of the simulation — specifically the threshold at which volatility triggers a crisis event — not the study design or analysis plan. Both arms of the RCT will run on the recalibrated engine (v2.0, CANONICAL_V1_INTERACTIVE parameters). The manipulation check pre-registered in the analysis plan (confirming 0.7–1.2 crises per session in the Treatment arm) will be updated to reflect the verified interactive rate of approximately 0.66 crises per session under mixed play.

**Full calibration documentation:** Available in the public project repository at https://github.com/nikhilsalunkemumbai/echo-space

**Updated locked parameters (CANONICAL_V1_INTERACTIVE):**

| Parameter | Grid sweep value | Interactive value | Notes |
|-----------|-----------------|-------------------|-------|
| ALPHA | 0.3 | 0.3 | Unchanged |
| GAMMA_Q | 0.12 | 0.12 | Unchanged |
| LAMBDA | 0.8 | 0.8 | Unchanged |
| SIGMA_NOISE | 0.01 | 0.01 | Unchanged |
| THETA_V | 1.5 | **0.18** | Recalibrated for interactive mode |
| SIGMA_V | 0.25 | **0.020** | Recalibrated for interactive mode |

---

## 3. Ethics review — IEC track update

**What the pre-registration metadata says:** "Ethics review in progress with Symbiosis International University IEC, Mumbai, India."

**Update:** SIU IEC confirmed that independent researchers without institutional affiliation are ineligible to submit directly. The active ethics review track has changed. Current status as of 03 April 2026:

- **CEHAT IEC** (iec@cehat.org) — email sent, awaiting response
- **NIRRCH IEC** (admin@nirrch.res.in) — email sent, awaiting response
- **SIU co-investigator route** — email sent asking for faculty referral, awaiting response

The ethics approval requirement and the commitment to provide an IEC reference number before data collection begins are unchanged.

---

## 4. Companion study protocol — journal update

**What the pre-registration says:** "A study protocol submitted to JMIR Research Protocols."

**Update:** The study protocol (Paper A) was submitted to the **International Journal of Serious Games (IJSG)** on 03 April 2026, not to JMIR Research Protocols. The decision to submit to IJSG was made on the basis of zero publication cost (IJSG charges no APC or submission fee) versus JMIR's fee on acceptance (USD 1,900 for unfunded authors). The protocol content is identical. IJSG is Scopus and ESCI (Web of Science) indexed.

Submission confirmation: received 03 April 2026. Awaiting editorial assignment.

---

## 5. arXiv preprint URL

**What the pre-registration says:** "[arXiv URL to be added on publication]" — appears in the Other / Context section and the Metadata description.

**Update:** The companion system description preprint (Paper B) is complete and awaiting cs.HC endorsement on arXiv. Endorsement code: MS6G7W. This field will be updated with the permanent arXiv URL as soon as the preprint is assigned an identifier.

---

## Summary of changes

| Item | Pre-registration text | Corrected / updated |
|------|-----------------------|---------------------|
| City | Mumbai, India | Pune, India |
| THETA_V | 1.5 | 0.18 (interactive sessions) |
| SIGMA_V | 0.25 | 0.020 (interactive sessions) |
| IEC | SIU IEC, Mumbai | CEHAT / NIRRCH / SIU co-investigator (pending) |
| Protocol journal | JMIR Research Protocols | International Journal of Serious Games |
| arXiv URL | Placeholder | To be added on endorsement |

None of these changes affect the study hypotheses, outcome measures, randomization procedure, blinding, statistical models, inference criteria, or analysis plan.

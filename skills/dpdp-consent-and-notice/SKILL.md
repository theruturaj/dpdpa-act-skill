---
name: dpdp-consent-and-notice
description: Notice standards, valid consent criteria, withdrawal mechanisms, Consent Managers, and legitimate uses under Chapter II (ss.4–7) of India's DPDP Act, 2023 and Rules 3–4 of the DPDP Rules, 2025. Use for drafting privacy notices, designing consent flows, evaluating non-consensual processing grounds, and managing Consent Manager integrations.
version: "1.0.0"
last_verified: "2026-11-05"
jurisdiction: "IN"
primary_statute: "Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023)"
subordinate_rules: "Digital Personal Data Protection Rules, 2025 (Notified 2025-11-13; Corrigendum 2025-12-16)"
commencement_status: "Phased (Section 6(9) & Rule 4 commencing 2026-11-13; Sections 4, 5, 6(1)-(8), 7 & Rule 3 commencing 2027-05-13)"
---

# DPDP Act 2023 – Consent, Notice, and Legitimate Uses (ss.4–7 & Rules 3–4)

Primary Sources:
- Statute: Digital Personal Data Protection Act, 2023 (ss.4–7).
- Subordinate Rules: DPDP Rules, 2025, Rule 3 (Notice requirements) and Rule 4 (Consent Managers).
- Notification: G.S.R. 843(E) (Commencement schedule).

---

## 1. Statutory Response Structure

When answering consent or notice questions, structure responses following:
1. **Legal Provision**: Section 4, 5, 6, or 7 of the DPDP Act and Rule 3 or 4 of the DPDP Rules, 2025.
2. **Plain-Language Interpretation**: Unambiguous explanation of compliance expectations.
3. **Applicable DPDP Rule**: Rule 3 notice items or Rule 4 Consent Manager registration terms.
4. **Commencement Status**:
   - Section 6(9) & Rule 4 (Consent Managers): **Phase 2 (Effective 13 November 2026)**.
   - Sections 4, 5, 6(1)–(8), (10), 7 & Rule 3: **Phase 3 (Effective 13 May 2027)**.
5. **Compliance Implications**: UI/UX design, consent logging, language options, withdrawal workflows.
6. **Exceptions & Exemptions**: Cross-reference Section 17 exemptions via `dpdp-board-enforcement`.
7. **Official Source References**: Citations to Section numbers and Gazette clauses.
8. **Legal Uncertainty & Interpretive Limitations**: Highlight pending operational guidelines from the Board.

---

## 2. Grounds for Processing (Section 4)
Personal data may only be processed for a lawful purpose (any purpose not expressly forbidden by law) through one of two distinct legal grounds:
1. **Consent-Based Processing (s.4(1)(a))**: The Data Principal has given valid consent in accordance with Section 6.
2. **Certain Legitimate Uses (s.4(1)(b))**: Non-consensual processing strictly falling within the statutory categories enumerated under Section 7.

---

## 3. Notice Requirements (Section 5 & Rule 3)

### Core Mandates:
Every request for consent must be accompanied or preceded by an itemized notice stating:
1. **Personal Data & Purpose**: Exact categories of personal data to be collected and the specific purpose for which each category will be processed (s.5(1)(i)).
2. **Exercise of Rights**: Clear instructions on how the Data Principal may exercise her right of withdrawal under Section 6(4) and her right to grievance redressal under Section 13 (s.5(1)(ii)).
3. **Board Complaints**: The manner in which the Data Principal may file a complaint with the Data Protection Board of India (s.5(1)(iii)).
4. **Contact Information**: Contact details of the Data Protection Officer (if an SDF) or authorized business contact person (s.6(3)).

### Language Access (s.5(3) & Rule 3):
- The Data Fiduciary must give the Data Principal the option to access the notice and consent request in **English or any of the 22 languages specified in the Eighth Schedule to the Constitution of India**.

### Legacy Data Notice (s.5(2)):
- Where consent was collected prior to the commencement of Section 5, the Data Fiduciary must issue the Section 5 notice to the Data Principal **as soon as reasonably practicable**.
- The Fiduciary may continue processing such legacy data until and unless the Data Principal withdraws consent.

---

## 4. Valid Consent Standards (Section 6)

### Four Pillars of Valid Consent (s.6(1)):
1. **Free**: Voluntary without coercion, bundling, or conditional access to unrelated services.
2. **Specific**: Directed strictly at a well-defined purpose.
3. **Informed**: Preceded by a compliant Section 5 notice.
4. **Unconditional & Unambiguous**: Indicated through a clear affirmative action (no pre-ticked boxes or implied consent).

### Purpose Limitation & Bundling Prohibitions (s.6(1)–(2)):
- Consent is valid only to the extent of data strictly necessary for the specified purpose.
- **Illustration**: If an online telemedicine app requires access to a user's contact list or photo library as a condition for medical consultation, consent for that contact list/photo library is invalid.
- Any provision in a consent agreement that waives statutory rights (such as complaining to the Board) is void (s.6(2)).

### Burden of Proof (s.6(10)):
- In any proceeding before the Board or Court, the **burden of proving** that valid notice was provided and valid consent was obtained rests entirely upon the **Data Fiduciary**.

---

## 5. Right of Withdrawal (Section 6(4)–(6))
- **Unconditional Right**: The Data Principal has the right to withdraw consent at any time.
- **Ease of Withdrawal**: The ease of withdrawing consent must be **comparable to the ease with which consent was given** (e.g. if granted in two clicks inside an app, withdrawal must be achievable in similar simple steps).
- **Consequences of Withdrawal**:
  - The Data Principal bears the consequences of withdrawal (e.g. cessation of service requiring that data).
  - Prior processing carried out lawfully remains valid.
  - Upon withdrawal, the Fiduciary must, within a reasonable time, cease processing and instruct its Data Processors to cease processing, unless continued retention is required under Indian law (s.6(6)).

---

## 6. Consent Managers (Section 6(7)–(9) & Rule 4)
*Enforcement Status: Commencing 13 November 2026 (Phase 2).*

- **Definition & Role**: An intermediary registered with the Data Protection Board of India acting as an accessible, transparent, and interoperable single point of contact for Data Principals to give, manage, review, and withdraw consent.
- **Fiduciary Accountability**: The Consent Manager is accountable directly to the Data Principal and acts strictly on her behalf.
- **Board Oversight**: The Board holds direct investigatory powers over Consent Managers under Section 27(1)(d) starting 13 November 2026.
- **Interoperability (Rule 4)**: Must adhere to open technical API standards, non-discriminatory registration criteria, and cryptographic audit trails for consent management.

---

## 7. Certain Legitimate Uses (Section 7) – No Consent Required

Processing without consent is permitted **strictly** under the following statutory grounds:
- **(a) Voluntary Provision**: The Data Principal voluntarily provides personal data for a specified purpose and has not indicated that she does not consent to its use (e.g. handing a business card to receive a quote).
- **(b) State Subsidies & Benefits**: Processing by the State or its instrumentalities for issuing subsidies, benefits, certificates, or licenses where prior consent exists or data is in notified databases.
- **(c) State Security & Legal Functions**: Functions of the State authorized by law, or in the interest of India's sovereignty, integrity, or security.
- **(d) Legal Disclosure to State**: Fulfilling a statutory legal obligation to disclose information to government bodies.
- **(e) Judicial Decrees & Orders**: Complying with any judgment, decree, or order of an Indian court, tribunal, or foreign civil/contractual order.
- **(f) Medical Emergency**: Responding to a medical emergency involving a threat to the life or immediate health of the Data Principal or any other individual.
- **(g) Epidemics & Public Health**: Medical treatment or health measures during an epidemic, pandemic, disease outbreak, or public health crisis.
- **(h) Disaster & Public Order**: Taking measures to ensure safety or provide assistance during disasters or breakdowns of public order.
- **(i) Employment Purposes**: Processing for employment purposes, or safeguarding the employer from loss or liability (preventing corporate espionage, protecting trade secrets, intellectual property), or providing employment benefits.

---

## 8. Cross-References & Related Skills
- Scope and Definitions: see `dpdp-act-overview`.
- Fiduciary obligations and security measures: see `dpdp-fiduciary-obligations`.
- Principal rights to access and erasure: see `dpdp-data-principal-rights`.
- Penalties for consent/notice violations (up to ₹50 crore under the Schedule): see `dpdp-board-enforcement`.

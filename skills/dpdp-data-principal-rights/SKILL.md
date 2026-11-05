---
name: dpdp-data-principal-rights
description: Rights and duties of Data Principals under Chapter III (ss.11–15) of India's DPDP Act, 2023 and Rules 10–12 of the DPDP Rules, 2025. Covers right to access information, correction, completion, erasure, grievance redressal exhaustion, nomination procedures, and statutory duties carrying penalties up to ₹10,000.
version: "1.0.0"
last_verified: "2026-11-05"
jurisdiction: "IN"
primary_statute: "Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023)"
subordinate_rules: "Digital Personal Data Protection Rules, 2025 (Notified 2025-11-13; Corrigendum 2025-12-16)"
commencement_status: "Phase 3 (Commencing 2027-05-13 under G.S.R. 843(E))"
---

# DPDP Act 2023 – Data Principal Rights and Duties (ss.11–15 & Rules 10–12)

Primary Sources:
- Statute: Digital Personal Data Protection Act, 2023, Sections 11, 12, 13, 14, 15.
- Subordinate Rules: DPDP Rules, 2025, Rules 10 (Access/Correction/Erasure procedures), 11 (Grievance redressal), and 12 (Nomination).
- Notification: G.S.R. 843(E) (Commencement schedule).

---

## 1. Statutory Response Structure

When answering questions regarding individual data rights or duties, AI agents must structure responses as follows:
1. **Legal Provision**: Cite Section 11, 12, 13, 14, or 15 of the Act and Rule 10, 11, or 12 of the DPDP Rules, 2025.
2. **Plain-Language Interpretation**: Explain what the individual is entitled to demand or required to fulfill.
3. **Applicable DPDP Rule**: Detail response formats, verification criteria, and timelines.
4. **Commencement Status**: **Phase 3 (Commencing 13 May 2027)** under Notification G.S.R. 843(E).
5. **Compliance Implications**: DSR (Data Subject Request) portals, identity verification, logging.
6. **Exceptions & Exemptions**: Carve-outs under Section 11(b)-(c) exceptions and Section 17.
7. **Official Source References**: Citations to statutory clauses and Gazette notifications.
8. **Legal Uncertainty & Interpretive Limitations**: Prescribed response windows and authentication standards.

---

## 2. Statutory Rights of Data Principals (Sections 11–14 & Rules 10–12)

Rights under Sections 11 and 12 are available against any Data Fiduciary to whom the Data Principal previously gave consent, or voluntarily provided data under Section 7(a).

### 1. Right to Access Information (Section 11 & Rule 10)
The Data Principal is entitled to obtain from the Data Fiduciary:
- **(a) Summary of Processing**: A summary of personal data being processed and the processing activities undertaken with respect to that data.
- **(b) Sharing Disclosure**: The identities of all other Data Fiduciaries and Data Processors with whom the personal data has been shared, along with a description of the personal data so shared.
- **(c) Prescribed Information**: Any other information as prescribed in the rules.
- **Law Enforcement Exception**: The identities of Data Fiduciaries with whom data was shared are **not** disclosed if the data was shared upon a written request authorized by law for the prevention, detection, or investigation of offences, cyber incidents, or prosecution.

### 2. Right to Correction and Erasure (Section 12 & Rule 10)
Upon receiving a request from the Data Principal:
- **Correction, Completion & Updating (s.12(1)–(2))**: The Fiduciary must correct inaccurate or misleading personal data, complete incomplete personal data, and update outdated personal data.
- **Erasure (s.12(3))**: The Fiduciary must erase personal data that is no longer necessary for the purpose for which it was processed, unless retention is mandated by law (e.g. banking KYC, tax compliance, or s.17 exemptions).

### 3. Right of Grievance Redressal (Section 13 & Rule 11)
- The Data Principal has the right to readily available means of grievance redressal provided by a Data Fiduciary or Consent Manager.
- **Mandatory Exhaustion Rule**: The Data Principal must first exhaust the grievance redressal mechanism of the Data Fiduciary or Consent Manager before approaching the Data Protection Board of India with a formal complaint under Section 27.
- The Fiduciary must respond to grievances within the timeframe prescribed under Rule 11.

### 4. Right to Nominate (Section 14 & Rule 12)
- The Data Principal has the right to nominate any other individual who shall, in the event of death or incapacity (unsoundness of mind or infirmity of body), exercise the rights of the Data Principal under the Act and Rules.

---

## 3. Statutory Duties of Data Principal (Section 15)

The DPDP Act is unique among global data protection statutes in imposing legally binding statutory duties directly on individuals:

1. **Compliance with Laws (s.15(a))**: Comply with the provisions of all applicable laws while exercising rights under the Act.
2. **No Impersonation (s.15(b))**: Not impersonate another person while providing personal data for a specified purpose.
3. **No Suppression in Official Documents (s.15(c))**: Not suppress any material information while providing personal data for any document, identifier, proof of identity, or address issued by the State or its instrumentalities.
4. **No False or Frivolous Complaints (s.15(d))**: Not register any false or frivolous grievance or complaint with a Data Fiduciary or the Data Protection Board of India.
   - The Board has the power to issue warnings or impose costs under Section 28(12).
5. **Authentic Information in DSRs (s.15(e))**: Furnish only such information as is verifiably authentic, while exercising the right to correction or erasure.

### Statutory Penalty for Breach of Duties:
- Under **Item 5 of the Schedule**, breach of any duty specified in Section 15 carries a financial penalty of up to **₹10,000**.

---

## 4. End-to-End Request Handling Flow for Organizations

1. **Authentication**: Verify the identity of the Data Principal or lawful guardian (for children under 18 per s.2(j)) in accordance with Rule 10.
2. **Grounds Check**: Confirm whether data was processed on consent (s.6) or voluntary provision (s.7(a)).
3. **Exemption & Retention Filter**: Check whether statutory retention mandates apply (e.g., s.8(7) legal retention, s.12(3) exceptions, s.17 state/judicial exemptions).
4. **Execution**: Update, correct, or erase data across primary databases and notify downstream Processors under contract.
5. **Response & Audit**: Deliver the summary within prescribed timelines; record complete audit logs of the transaction.
6. **Escalation**: If unresolved, direct the applicant to the internal grievance channel and, upon exhaustion, to the Data Protection Board of India.

---

## 5. Cross-References & Related Skills
- Definitions and parental representation rules: see `dpdp-act-overview`.
- Grounds for processing and withdrawal rights: see `dpdp-consent-and-notice`.
- Fiduciary retention duties and technical safeguards: see `dpdp-fiduciary-obligations`.
- Complaint proceedings before the Board and TDSAT appeals: see `dpdp-board-enforcement`.

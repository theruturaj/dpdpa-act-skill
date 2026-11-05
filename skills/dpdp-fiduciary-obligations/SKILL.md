---
name: dpdp-fiduciary-obligations
description: Core obligations of Data Fiduciaries under Sections 8–10 of India's DPDP Act, 2023 and Rules 5–9 of the DPDP Rules, 2025. Covers technical safeguards, breach notification protocols, retention/erasure rules, Data Processor contracts, children's data restrictions, and Significant Data Fiduciary (SDF) requirements.
version: "1.0.0"
last_verified: "2026-11-05"
jurisdiction: "IN"
primary_statute: "Digital Personal Data Protection Act, 2023 (Act No. 22 of 2023)"
subordinate_rules: "Digital Personal Data Protection Rules, 2025 (Notified 2025-11-13; Corrigendum 2025-12-16)"
commencement_status: "Phase 3 (Commencing 2027-05-13 under G.S.R. 843(E))"
---

# DPDP Act 2023 – Data Fiduciary Obligations (ss.8–10 & Rules 5–9)

Primary Sources:
- Statute: Digital Personal Data Protection Act, 2023, Sections 8, 9, 10.
- Subordinate Rules: DPDP Rules, 2025, Rules 5 (Children's consent), 6 (Security safeguards), 7 (Breach intimation), 8 (Retention & erasure), and 9 (Significant Data Fiduciaries).
- Notification: G.S.R. 843(E) (Commencement schedule).

---

## 1. Statutory Response Structure

When advising on fiduciary compliance, AI agents must structure responses as follows:
1. **Legal Provision**: Cite Section 8, 9, or 10 of the Act and corresponding Rules 5–9 of the DPDP Rules, 2025.
2. **Plain-Language Interpretation**: Explain the technical and operational compliance obligation.
3. **Applicable DPDP Rule**: Detail prescribed forms, notifications timelines, or audit frameworks.
4. **Commencement Status**: **Phase 3 (Commencing 13 May 2027)** under Notification G.S.R. 843(E).
5. **Compliance Implications**: Technical architecture, vendor contracting, breach playbooks, audit trails.
6. **Exceptions & Exemptions**: Cross-reference Section 17 (e.g. startup exemptions under s.17(3)).
7. **Official Source References**: Citations to Act sections, Rule numbers, and penalty Schedule items.
8. **Legal Uncertainty & Interpretive Limitations**: Note upcoming SDF classification lists and notification templates.

---

## 2. General Obligations of Data Fiduciary (Section 8 & Rules 6–8)

The Data Fiduciary is responsible for statutory compliance notwithstanding any contrary agreement, including for processing conducted by its Data Processors (s.8(1)).

### Ten Mandatory Duties:
1. **Processor Engagement under Contract (s.8(2))**: May engage, appoint, or involve a Data Processor only under a valid, written contract for activities related to offering goods or services to Data Principals.
2. **Data Accuracy & Consistency (s.8(3))**: Where data is used to make a decision that affects the Data Principal, or disclosed to another Data Fiduciary, the Fiduciary must ensure complete, accurate, and consistent data.
3. **Technical & Organizational Measures (s.8(4))**: Implement appropriate technical and organizational measures to ensure effective compliance with the Act and Rules.
4. **Reasonable Security Safeguards (s.8(5) & Rule 6)**: Take reasonable security safeguards (including robust access controls, encryption, vulnerability assessments, and logging) to prevent personal data breaches.
   - *Penalty exposure for failure*: Up to **₹250 crore** (Schedule, Item 1).
5. **Personal Data Breach Intimation (s.8(6) & Rule 7)**: In the event of a personal data breach, the Fiduciary must notify:
   - The **Data Protection Board of India**; and
   - Each **affected Data Principal**, in the form and manner prescribed under Rule 7 without undue delay.
   - *Penalty exposure for failure*: Up to **₹200 crore** (Schedule, Item 2).
6. **Erasure upon Purpose Cessation or Withdrawal (s.8(7) & Rule 8)**: Erase personal data (and cause Processors to erase) upon the Data Principal withdrawing consent or as soon as it is reasonable to assume that the specified purpose is no longer being served, whichever is earlier.
   - *Exception*: Retention required under Indian law (e.g., PMLA, RBI KYC directions, IT Act tax records).
7. **Deemed Cessation of Purpose (s.8(8) & Rule 8)**: The specified purpose is deemed no longer served when the Data Principal has neither approached the Fiduciary nor exercised rights for the prescribed period.
   - Section 8(11) defines "approach" as initiating contact in person or by electronic/physical communication.
8. **Publication of Business Contact Information (s.8(9))**: Publish the business contact details (name, email, address) of the Data Protection Officer (if an SDF) or another authorized point of contact capable of answering questions about processing.
9. **Grievance Redressal Mechanism (s.8(10))**: Establish and maintain an effective and readily accessible grievance redressal mechanism.

---

## 3. Children's Data & Persons with Disability (Section 9 & Rule 5)

*Statutory definition*: "Child" means an individual who has not completed 18 years of age (s.2(f)).

### Core Mandates:
1. **Verifiable Parental Consent (s.9(1) & Rule 5)**: Before processing any personal data of a child or a person with disability who has a lawful guardian, obtain verifiable consent of the parent or lawful guardian in the prescribed manner.
2. **Prohibition of Detrimental Processing (s.9(2))**: Never undertake any processing of personal data that is likely to cause any detrimental effect on the well-being of a child.
3. **Ban on Tracking & Targeted Advertising (s.9(3))**: Never undertake:
   - Tracking or behavioral monitoring of children; or
   - Targeted advertising directed at children.
4. **Penalty Exposure**: Up to **₹200 crore** for breach of Section 9 obligations (Schedule, Item 3).

### Exemptions & Safe Harbors (s.9(4)–(5)):
- The Central Government may exempt specific classes of Fiduciaries or specific processing purposes under Section 9(4).
- The Central Government may notify a lower age threshold or exempt age limit for certain Fiduciaries that establish verifiably safe processing mechanisms (s.9(5)).

---

## 4. Significant Data Fiduciaries (Section 10 & Rule 9)

The Central Government designates Significant Data Fiduciaries (SDFs) based on:
- Volume and sensitivity of personal data processed.
- Risk of harm to the rights of Data Principals.
- Potential impact on the sovereignty, integrity, and security of India.
- Risk to electoral democracy and public order.

### Additional SDF Mandatory Duties:
1. **Resident Data Protection Officer (s.10(2)(a))**: Appoint a Data Protection Officer (DPO) who must:
   - Be an individual based in India;
   - Be answerable directly to the Board of Directors or governing body; and
   - Serve as the point of contact for grievance redressal under the Act.
2. **Independent Data Auditor (s.10(2)(b))**: Appoint an independent data auditor to evaluate compliance with the Act.
3. **Data Protection Impact Assessment (DPIA) (s.10(2)(c)(i) & Rule 9)**: Conduct periodic DPIAs detailing risk mitigation and rights safeguards.
4. **Periodic Compliance Audits (s.10(2)(c)(ii))**: Undertake regular data protection audits by external accredited auditors.
5. **Penalty Exposure**: Up to **₹150 crore** for breach of SDF obligations (Schedule, Item 4).

---

## 5. Fiduciary Compliance Checklist

- [ ] Execute Data Processing Agreements (DPAs) with all vendors processing digital personal data.
- [ ] Implement Technical & Organizational Safeguards (AES-256 encryption, MFA, access logging).
- [ ] Establish an Automated Breach Incident Playbook for Dual Intimation (Board + Data Principals).
- [ ] Formulate a Purpose-Linked Retention and Erasure Schedule.
- [ ] Deploy Verifiable Parental Consent verification for users under 18.
- [ ] Disable behavioral tracking, profiling, and targeted ads for child accounts.
- [ ] Publish clear business contact details for grievance handling.
- [ ] (If designated SDF): Appoint India-based DPO, retain independent auditor, schedule DPIAs.

---

## 6. Cross-References & Related Skills
- Master overview, definitions, and scope: see `dpdp-act-overview`.
- Notice and consent requirements: see `dpdp-consent-and-notice`.
- Data Principal rights (access, correction, erasure): see `dpdp-data-principal-rights`.
- Exemptions under Section 17 and Board enforcement: see `dpdp-board-enforcement`.

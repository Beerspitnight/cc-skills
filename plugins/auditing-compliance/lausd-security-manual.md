
IT Security
## Compliance Manual
## Version 2.0
## Published October 2025

Below are the current policy documents that govern the District’s Information Security Program. Users of
the District’s networks are expected to strictly adhere to these policies, and failure to do so could result
in an investigation and the issuance of notices of non-compliance.


## Summary:
# LAUSD IT Security Compliance Manual v2.0 (Reference)
**Based on NIST CSF 2.0 | Published October 2025**

This document maps NIST CSF 2.0 Controls to LAUSD Bulletins (BUL) and Reference Guides (REF). Use this to provide official citations for audit findings.

## 1. GOVERN (GV)

### Organizational Context (GV.OC)
*   **GV.OC-01 (Mission):** BUL-101556.0 Information Security Policy
*   **GV.OC-03 (Legal/Privacy):** REF-060700 (UDIPP/PoDs), BUL-5181.3 (Internet Safety)
*   **GV.OC-05 (Critical Services):** BUL-1077 (Info Protection), BUL-5242.1 (Web Filtering)

### Risk Management (GV.RM)
*   **GV.RM-01 (Objectives):** BUL-101556.0 Information Security Policy
*   **GV.RM-05 (Supply Chain Comms):** BUL-157711 (Incident Mgmt), REF-060700 (UDIPP)

### Roles & Responsibilities (GV.RR)
*   **GV.RR-01 (Leadership Accountability):** BUL-114700.1 (Access to Critical Systems), BUL-999.15 (Responsible Use)
*   **GV.RR-04 (HR Practices):** BUL-050298.1 (Fingerprinting), BUL-0791141 (Security Training)

### Supply Chain Risk Management (GV.SC)
*   **GV.SC-01 (Supply Chain Strategy):** Codebase must mitigate supply chain attacks (e.g., lockfiles).
    *   *Policy:* BUL-1553 (Security Standards), REF-060700 (UDIPP), BUL-6916.1 (Data Destruction).
*   **GV.SC-04/05 (Supplier Requirements):** BUL-114700.1 (Access Control), BUL-1553.

## 2. IDENTIFY (ID)

### Asset Management (ID.AM)
*   **ID.AM-1/2 (Hardware/Software Inventory):** Software Bill of Materials (SBOM) or manifests required.
    *   *Policy:* BUL-1891.0 (Data Center Inv), BUL-114700.1 (Critical Systems), BUL-2424.4 (Web Mgmt).
*   **ID.AM-5 (Asset Prioritization):** BUL-1077 (Info Protection Policy).
*   **ID.AM-8 (Lifecycle Mgmt):** BUL-6916.1 (Data Destruction).

### Risk Assessment (ID.RA)
*   **ID.RA-01 (Vulnerabilities):** BUL-129101.1 (Vulnerability Mgmt Policy).
*   **ID.RA-09 (Auth/Integrity Check):** REF-060700 (UDIPP).

## 3. PROTECT (PR)

### Identity Management (PR.AA)
*   **PR.AA-01 (Identity Mgmt):** BUL-079114.1 (Training), BUL-114700.1 (Access).
*   **PR.AA-03 (Authentication):** Must use OIDC/SAML. Local passwords discouraged.
    *   *Policy:* BUL-1597.0 (VPN), BUL-114700.1 (Access to Critical Systems).
*   **PR.AA-05 (Access/Least Privilege):** BUL-114700.1, BUL-1597.0.

### Data Security (PR.DS)
*   **PR.DS-01 (Data at Rest):** Encryption/Hashing required for PII.
    *   *Policy:* REF-3757.0 (Security Standards), BUL-101556.0.
*   **PR.DS-02 (Data in Transit):** TLS/SSL `ssl=true` enforcement required.
    *   *Policy:* REF-3757.0, BUL-5242.1 (Web Filtering).
*   **PR.DS-11 (Backups):** BUL-6916.1 (Data Destruction), DR/BC Test Plan.

### Platform Security (PR.PS)
*   **PR.PS-01 (Config Mgmt):** BUL-106900.1 (Change Mgmt).
*   **PR.PS-04 (Logging):** Logs must be generated for continuous monitoring.
    *   *Policy:* REF-3757.0, BUL-114700.1.
*   **PR.PS-06 (Secure Development):** No hardcoded secrets.
    *   *Policy:* REF-3757.0, BUL-716.1 (Copyright/Software).

## 4. DETECT (DE)

### Continuous Monitoring (DE.CM)
*   **DE.CM-01/02/03 (Monitoring):** Systems must monitor for adverse events (Logs).
    *   *Policy:* BUL-129101.1 (Vulnerability Mgmt).
*   **DE.CM-09 (Runtime Monitoring):** BUL-129101.1.

### Privacy Constraints (from Intro/BUL-1077)
*   **BUL-1077:** Logs **MUST NOT** contain PII (Student IDs, Names, Emails).

## 5. RESPOND (RS)

### Incident Management (RS.MA)
*   **RS.MA-01 (Plan Execution):** Repository must define reporting process (`SECURITY.md`).
    *   *Policy:* BUL-157711 (Incident Mgmt Policy), Incident Response Plan.
*   **RS.MA-02 (Triage):** BUL-157711.

### Reporting (RS.CO)
*   **RS.CO-02 (Notification):** BUL-157711.

## 6. RECOVER (RC)

### Recovery Execution (RC.RP)
*   **RC.RP-01 (Recovery Plan):** Repository must have backups/DR plan.
    *   *Policy:* BUL-157711, BUL-1553, Business Continuity Plan.

## Document Type
## Synopsis
## BULLETINS

BUL K-24.1 LAUSD Firewall Policy
Governs how the firewalls will filter Internet traffic
to mitigate the risks and losses with security threats to Los Angeles
Unified School District’s (District) network and information systems.
BUL-714.0 Compliance with the 1976 US
## Copyright Law
Outlines employee obligations to comply with the 1976 Copyright law.
BUL-716.1 Compliance with the 1976 US
Copyright Law-Computer Software
Outlines employee obligations to comply with the 1976 Copyright law in
acquiring, using, and distributing software.
BUL-999.16 Responsible Use Policy
(RUP) for District Computer and
## Network Systems
Outlines acceptable use rules for students, parents, and staff using
District-owned devices, networks, internet, and digital tools.
BUL-1077.2 Information Protection
## Policy

Establishes information security levels and sets the minimum
requirements for protecting sensitive information (student, employee,
operational) throughout its lifecycle (creation, use, transmission, storage,
disposal).
BUL-1553.1 Security Standards for
## Networked Computer Systems
Reinforces standards for managing confidentiality, integrity, and
availability of information systems that handle sensitive District data.

Contents i


## Housing Confidential Information
BUL-1597.0 Acceptable Use Policy for
ITD Virtual Private Network (VPN)
## Services
Defines usage policies, restrictions, and user responsibilities for staff
using District VPN services for remote access.
BUL-1891.0 ITD Data Center Inventory
## Change Notification Policy
Requires departments to notify ITS of any infrastructure or equipment
changes within the data center to maintain inventory and risk tracking.
BUL-2424.4 Website Development and
## Management
Provides the procedures, requirements, and responsibilities for
schools and offices when using websites to communicate District
information.
BUL-3872.2 Fingerprinting and
Criminal Background Compliance for
## Contractors
Requires contractors and vendors to complete fingerprinting and
background checks prior to gaining access to school campuses or student
data.
BUL-5181.3 Policy Regarding Internet
Safety for Students
Requires all students who are provided access to the Internet to
participate in an Internet Safety Education Program provided by
teachers, administrators, and staff.
BUL-5242.0 Web Content Filtering
## Policy

Describes how the District complies with CIPA requirements to take
measures to block access to web sites that are (a) obscene, (b) child
pornography, or (c) harmful to minors through the implementation of
solutions that inspects web content and filter or blocks any inappropriate
web sites.
BUL-6916.1 Data Destruction and
## Disposal
Specifies the secure destruction methods and documentation process for
various media including physical and virtual devices containing sensitive
data.
BUL-050298.1 Fingerprinting
Requirements and Procedures
Defines fingerprinting and DOJ clearance requirements for employees
and volunteers to ensure student and staff safety.
REF-060700 Unified Digital
## Instructional Procurement Plan
(UDIPP/PoDs)
Outlines standards and procedures for selecting and procuring digital
instructional content and platforms to ensure security, interoperability,
and compliance.
BUL-0791141 Information Security
Awareness and Training Policy
Mandates annual cybersecurity awareness training for all employees and
outlines responsibilities for completing and tracking compliance.
BUL-095100.3 Site Computer
## Inventory Policy
Establishes mandatory procedures for cataloging, securing, tracking, and
certifying all computers and related IT assets across the District.
BUL-106900.1 Change Management
for Critical Information Systems (2)
Outlines formal procedures to request, evaluate, and approve changes to
production systems to reduce risk and ensure service continuity.
BUL-114700.1 Access to Critical
## Information Systems
Defines access controls, approval processes, and authorization
requirements for accessing critical systems like MiSiS or SAP.
BUL-129101.1 Vulnerability
## Management Policy
Establishes the process for identifying, prioritizing, remediating, and
reporting vulnerabilities in District systems and networks.
BUL-157711 Incident Management
## Policy
Establishes procedures for identifying, reporting, managing, and resolving
cybersecurity and IT service incidents. Includes roles, severity levels, and
escalation paths.
BUL-101556.0 Information Security Policy
Overarching compliance policy.
REF-1438.3 - How to Obtain a District
Provides guidance for requesting and provisioning LAUSD Single Sign-On
and email accounts, including eligibility and support procedures.


Single Sign-On and E-mail Account

## REFERENCE GUIDES
REF-3757.1 Description of Security
Standards for Networked Computer
## Systems Housing Confidential
## Information
Details baseline security controls (encryption, access, monitoring)
required for any system that stores or processes confidential
information.
REF-4686.0 Description of Security
Standards for Installation of Building
Automation Systems on the LAUSD
## Network
Details security requirements for HVAC, lighting, and other building
control systems integrated into the LAUSD network.
## PLANS
## Business Continuity Plan
(Contact GRC for access)
Defines contingency procedures and recovery strategies to restore
critical operations and IT services during a major disruption or disaster.
## Incident Response Plan
(Contact GRC for access)
Defines operational plan detailing technical and procedural steps in
preparation of and during a security incident, including testing controls,
containment, eradication, recovery, communication, and reporting.
## STANDARD OPERATION PROCEDURES
## (SOP)


The above policies have been mapped and organized in accordance with the National Institute of
Standards and Technology Cybersecurity Framework (NIST CSF). Within this manual, the policies have
been crossed referenced six NIST CSF functions listed below:

Govern (GV): Establishing and monitoring the District’s cybersecurity risk management strategy,
expectations, and policy.
Identify (ID): Developing a holistic understanding of cybersecurity risks including systems,
assets, data, and capabilities enabling informed decision-making with regards to cybersecurity
priorities and resource allocations.
Protect (PR): Using safeguards to prevent or reduce cybersecurity risk.
Detect (DE): Finding and analyzing possible cybersecurity attacks and compromises.
Respond (RS): Taking action regarding a detected cybersecurity incident.
Recover (RC): Restoring assets and operations that may be impacted by a cybersecurity
incident.

This manual and policies will be reviewed and updated on an annual basis or as needed by the CIO and CISO. For
additional information contact GRC Team at ITSec-GRC@lausd.net


## 2


## NIST FUNCTION:
## Govern
Govern: Organizational Context (GV.OC)


This section establishes and monitors the District’s cybersecurity risk management strategy,
expectations, and policy. Governance activities are critical for incorporating cybersecurity into the
District’s broader enterprise risk management strategy. GOVERN directs an understanding of
organizational context; the establishment of cybersecurity strategy and cybersecurity supply chain risk
management; roles, responsibilities; and the oversight of cybersecurity strategy. Links to District
Bulletins and Standard Operating Procedures (SOPs) are provided.

GV.OC-01 The District’s organizational mission is understood and informs
cybersecurity risk management
## • Mission Statement
- BUL-101556.0 Information Security Policy
- Information Risk Management Framework (Contact GRC)

GV.OC-02 Internal and external stakeholders are understood, and their needs and
expectations regarding cybersecurity risk management are understood and
considered
- BUL-114700.1 Access to Critical Information Systems
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-5181.3 Internet Safety for Students

GV.OC-03 Legal, regulatory, and contractual requirements regarding cybersecurity—
including privacy and civil liberties obligations—are understood and managed
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-5181.3 Internet Safety for Students

GV.OC-04 Critical objectives, capabilities, and services that stakeholders depend on or
expect from the organization are understood and communicated – For
incident response
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC)

## 3



GV.OC-05 Critical objectives, capabilities, and services that stakeholders depend on or
expect from the organization are understood and communicated –
identification of critical information
- BUL-101556.0 Information Security Policy
- BUL-1077 Information Protection Policy
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-5181.3 Internet Safety for Students

## 4


Govern: Risk Management Strategy (GV.RM)


GV.RM-01 Risk management objectives are established and agreed to by organizational
stakeholders
- Information Security Risk Management Framework (Contact GRC)
- Information Security Risk Assessment Process Information Technology Services (ITS)
Policies, Standards, and Procedures
- BUL-101556.0 Information Security Policy

GV.RM-02 Risk appetite and risk tolerance statements are established, communicated, and
maintained
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

GV.RM-03 Cybersecurity risk management activities and outcomes are included in enterprise
risk management processes
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

GV.RM-04 Strategic direction that describes appropriate risk response options is established
and communicated
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

GV.RM-05 Lines of communication across the organization are established for cybersecurity
risks, including risks from suppliers and other third parties
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for access)
- Third-Party - Supply Chain Risk Procedures
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-5181.3 Internet Safety for Students

GV.RM-06 A standardized method for calculating, documenting, categorizing, and prioritizing
cybersecurity risks is established and communicated
- Information Security Risk Management Framework (Contact GRC)
- Information Security Risk Assessment Process SOP
BUL-101556.0 Information Security Policy

GV.RM-07 Strategic opportunities (i.e., positive risks) are characterized and are included in
organizational cybersecurity risk discussions

## 5


- Information Security Risk Management Framework (Contact GRC)
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

## 6


Govern: Roles, Responsibilities, and Authorities (GV.RR)


GV.RR-01 Organizational leadership is responsible and accountable for cybersecurity risk
and fosters a culture that is risk-aware, ethical, and continually improving
- REF-1438.3 - How to Obtain a District Single Sign-On and E-mail Account
- BUL-114700.1 Access to Critical Information Systems
- BUL-0791141 Information Security Awareness and Training Policy
- BUL-999.15 Responsible Use Policy () for District Computer and Network Systems
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-5181.3 Internet Safety for Students
- BUL-101556.0 Information Security Policy

GV.RR-02 Roles, responsibilities, and authorities related to cybersecurity risk management
are established, communicated, understood, and enforced
- REF-1438.3 - How to Obtain a District Single Sign-On and E-mail Account
- BUL-114700.1 Access to Critical Information Systems
- BUL-0791141 Information Security Awareness and Training Policy
- BUL-999.15 Responsible Use Policy () for District Computer and Network Systems
- BUL-2424.4 Website Development and Management
- BUL-101556.0 Information Security Policy

GV.RR-03 Adequate resources are allocated commensurate with the cybersecurity risk
strategy, roles, responsibilities, and policies
- Information Security Risk Management Framework (Contact GRC)
- Information Security Risk Assessment Process SOP
- REF-1438.3 - How to Obtain a District Single Sign-On and E-mail Account
- BUL-114700.1 Access to Critical Information Systems
- BUL-5242.1 Web Content Filtering Policy
- BUL-5181.3 Internet Safety for Students
- BUL-101556.0 Information Security Policy

GV.RR-04 Cybersecurity is included in human resources practices
- BUL-050298.1 Fingerprinting Requirements and Procedures
- BUL-3872.1 Fingerprinting and Criminal Background Compliance for Contractors
- BUL-0791141 Information Security Awareness and Training Policy
- REF-1438.3 - How to Obtain a District Single Sign-On and E-mail Account
- BUL-114700.1 Access to Critical Information Systems
- BUL-101556.0 Information Security Policy


## 7





## 8


Govern: Policy (GV.PO)


GV.PO-01 Policy for managing cybersecurity risks is established based on organizational
context, cybersecurity strategy, and priorities and is communicated and enforced
- How to Obtain a District Single Sign-On and E-mail Accounts
- BUL-0791141 Information Security Awareness and Training Policy
- BUL-114700.1 Access to Critical Information Systems
- BUL-050298.1 Fingerprinting Requirements and Procedures
- BUL-3872.1 Fingerprinting and Criminal Background Compliance for Contractors

GV.PO-02 Policy for managing cybersecurity risks is reviewed, updated, communicated,
and enforced to reflect changes in requirements, threats, technology, and
organizational mission
- How to Obtain a District Single Sign-On and E-mail Accounts
- BUL-0791141 Information Security Awareness and Training Policy
- BUL-114700.1 Access to Critical Information Systems
- BUL-050298.1 Fingerprinting Requirements and Procedures
- BUL-3872.1 Fingerprinting and Criminal Background Compliance for Contractors

Govern: Oversight (GV.OV)


GV.OV-01 Cybersecurity risk management strategy outcomes are reviewed to inform and
adjust strategy and direction
- Information Security Risk Management Framework (Contact GRC)
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

GV.OV-02 The cybersecurity risk management strategy is reviewed and adjusted to ensure
coverage of organizational requirements and risks
- Information Security Risk Management Framework (Contact GRC)
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

GV.OV-03 Organizational cybersecurity risk management performance is evaluated and
reviewed for adjustments needed
- Information Security Risk Management Framework (Contact GRC)
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

## 9


Govern: Cybersecurity Supply Chain Risk Management (GV.SC)


GV.SC-01 A cybersecurity supply chain risk management program, strategy,
objectives, policies, and processes are established and agreed to by
organizational stakeholders
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures

GV.SC-02 Cybersecurity roles and responsibilities for suppliers, customers, and partners are
established, communicated, and coordinated internally and externally
- BUL-0791141 Information Security Awareness and Training Policy
- BUL-101556.0 Information Security Policy
- BUL-999.16 Responsible Use Policy (RUP) for District Computer and Network Systems
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures

GV.SC-03 Cybersecurity supply chain risk management is integrated into cybersecurity and
enterprise risk management, risk assessment, and improvement processes
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures

GV.SC-04 Suppliers are known and prioritized by criticality
- BUL-114700.1 Access to Critical Information Systems
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential

## 10


## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures

GV.SC-05 Requirements to address cybersecurity risks in supply chains are established,
prioritized, and integrated into contracts and other types of agreements with
suppliers and other relevant third parties
- BUL-114700.1 Access to Critical Information Systems
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures

GV.SC-06 Planning and due diligence are performed to reduce risks before entering into
formal supplier or other third-party relationships
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures


## 11


GV.SC-07 The risks posed by a supplier, their products and services, and other third parties
are understood, recorded, prioritized, assessed, responded to, and monitored over
the course of the relationship
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures

GV.SC-08 Relevant suppliers and other third parties are included in incident planning,
response, and recovery activities
- BUL-157711 Incident Management Policy
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures

GV.SC-09  Supply chain security practices are integrated into cybersecurity and enterprise
risk management programs, and their performance is monitored throughout the
technology product and service life cycle
- BUL-114700.1 Access to Critical Information Systems
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures

GV.SC-10 Cybersecurity supply chain risk management plans include provisions for activities
that occur after the conclusion of a partnership or service agreement
- BUL-114700.1 Access to Critical Information Systems
- Information Security Risk Management Framework (Contact GRC)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information

## 12


- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)
- Third-Party - Supply Chain Risk Procedures



## 8


## NIST FUNCTION:
## Identify
Identify: Asset Management (ID.AM)

This section helps identify the current cybersecurity risk to the District. Understanding District assets
(e.g., data, hardware, software, systems, facilities, services, people) and the related cybersecurity risks
enables the District to focus and prioritize its efforts in a manner consistent with its risk management
strategy and the mission needs identified under GOVERN. This Function also includes the identification of
improvements needed for the District’s policies, processes, procedures, and practices supporting
cybersecurity risk management to inform efforts under all six Functions. Links to District Bulletins and
Standard Operating Procedures (SOPs) are provided.

ID.AM-1 Inventories of hardware managed by the organization are maintained
- BUL-1891.0 ITD Data Center Inventory Change Notification Policy
- BUL-095100.2 Site Computer Inventory Policy
- BUL-114700.1 Access to Critical Information Systems
- BUL-999.16 Responsible Use Policy (RUP) for District Computer and Network Systems
- BUL-101556.0 Information Security Policy

ID.AM-2 Inventories of software, services, and systems managed by the organization are
maintained
- BUL-114700.1 Access to Critical Information Systems
- BUL-999.16 Responsible Use Policy (RUP) for District Computer and Network Systems
- BUL-2424.4 Website Development and Management
- BUL-101556.0 Information Security Policy

ID.AM-3 Representations of the organization's authorized network communication and
internal and external network data flows are maintained
- REF-3757 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)

ID.AM-4 Inventories of services provided by suppliers are maintained
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)

ID.AM-5 Assets are prioritized based on classification, criticality, resources, and impact on
the mission

## 9


- BUL-1077 Information Protection Policy
- BUL-101556.0 Information Security Policy

## 10


ID.AM-6 Withdrawn NIST CSF 2.0

ID.AM-7 Inventories of data and corresponding metadata for designated data types are
maintained
- BUL-1077 Information Protection Policy
- BUL-101556.0 Information Security Policy

ID.AM-8 Systems, hardware, software, services, and data are managed throughout their
life cycles
- BUL-114700.1 Access to Critical Information Systems
- BUL-6916.1 Data Destruction and Disposal
- BUL-1597.0 Acceptable Use Policy for ITD Virtual Private Network (VPN) Services

Identify: Risk Assessment (ID.RA)


ID.RA-01 Vulnerabilities in assets are identified, validated, and recorded
- REF-4686.0 Description of Security Standards for Installation of Building Automation
Systems on the LAUSD Network
- BUL-129101.1 Vulnerability Management Policy

ID.RA-02 Cyber threat intelligence is received from information sharing forums and sources
- BUL-129101.1 Vulnerability Management Policy
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

ID.RA-03 Internal and external threats to the organization are identified and recorded
- BUL-129101.1 Vulnerability Management Policy
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

ID.RA-04 Potential impacts and likelihoods of threats exploiting vulnerabilities are identified
and recorded
- BUL-129101.1 Vulnerability Management Policy
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- Information Security Risk Assessment Process SOP


## 11



ID.RA-05 Threats, vulnerabilities, likelihoods, and impacts are used to understand inherent
risk and inform risk response prioritization
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-101556.0 Information Security Policy

ID.RA-06 Risk responses are chosen, prioritized, planned, tracked, and communicated
- BUL-129101.1 Vulnerability Management Policy
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- Information Security Risk Assessment Process SOP
## • Risk Management Strategy
- BUL-101556.0 Information Security Policy

ID.RA-07 Changes and exceptions are managed, assessed for risk impact, recorded,
and tracked
- BUL-129101.1 Vulnerability Management Policy
- Information Security Risk Assessment Process SOP
## • Risk Management Strategy
- BUL-106900.1 Change Management for Critical Information Systems (2)
ID.RA-08 Processes for receiving, analyzing, and responding to vulnerability disclosures are
established
- BUL-129101.1 Vulnerability Management Policy
- Information Security Risk Assessment Process SOP
- BUL-101556.0 Information Security Policy

ID.RA-09 The authenticity and integrity of hardware and software are assessed prior to
acquisition and use
- BUL-114700.1 Access to Critical Information Systems
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)

ID.RA-10 Critical suppliers are assessed prior to acquisition
- BUL-114700.1 Access to Critical Information Systems
- REF-060700 Unified Digital Instructional Procurement Plan (UDIPP/PoDs)

Identify: Improvement (ID.IM)


ID.IM-01 Improvements are identified from evaluations
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

## 12





ID.IM-02 Improvements are identified from security tests and exercises, including those
done in coordination with suppliers and relevant third parties
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

ID.IM-03 Improvements are identified from execution of operational processes, procedures,
and activities
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
ID.IM-04 Incident response plans and other cybersecurity plans that affect operations are
established, communicated, maintained, and improved
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)


## 13


## NIST FUNCTION:
## Protect
Protect: Identity Management and Access Control (PR.AA)

This section addresses District’s safeguards to prevent or reduce cybersecurity risk. Once assets and risks
are identified and prioritized, PROTECT supports the ability to secure those assets to prevent or lower
the likelihood and impact of adverse cybersecurity events. Outcomes covered by this Function include
awareness and training; data security; identity management, authentication, and access control;
platform security (i.e., securing the hardware, software, and services of physical and virtual platforms);
and the resilience of technology infrastructure. Links to District Bulletins and Standard Operating
Procedures (SOPs) are provided.

PR.AA-01 Identities and credentials for authorized users, services, and hardware are
managed by the organization
- BUL-079114.1 Information Security Training And Awareness
- BUL-114700.1 Access to Critical Information Systems
- BUL-6916.1 Data Destruction and Disposal
- BUL-5242.1 Web Content Filtering Policy
- BUL-K-24.1 LAUSD Firewall Policy

PR.AA-02 Identities are proofed and bound to credentials based on the context of interactions
- BUL-114700.1 Access to Critical Information Systems
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-K-24.1 LAUSD Firewall Policy

PR.AA-03 Users, services, and hardware are authenticated
- BUL-1597.0 Acceptable Use Policy for ITD Virtual Private Network (VPN) Services
- BUL-114700.1 Access to Critical Information Systems
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-K-24.1 LAUSD Firewall Policy

PR.AA-04 Identity assertions are protected, conveyed, and verified
- BUL-114700.1 Access to Critical Information Systems
- BUL-5242.1 Web Content Filtering Policy

## 14



- BUL-K-24.1 LAUSD Firewall Policy

PR.AA-05 Access permissions, entitlements, and authorizations are defined in a policy,
managed, enforced, and reviewed, and incorporate the principles of least privilege
and separation of duties
- BUL-114700.1 Access to Critical Information Systems
- BUL-6916.1 Data Destruction and Disposal
- BUL-1597.0 Acceptable Use Policy for ITD Virtual Private Network (VPN) Services
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-K-24.1 LAUSD Firewall Policy

PR.AA-06 Physical access to assets is managed, monitored, and enforced commensurate
with risk
- Photo Identification Badges and Access Policy
- Policy for Requesting Security Access Data At LAUSD Administrative Headquarters
- BUL-101556.0 Information Security Policy

Protect: Awareness and Training (PR.AT)


PR.AT-01 Personnel are provided with awareness and training so that they possess the
knowledge and skills to perform general tasks with cybersecurity risks in mind
- BUL-079114.1 Information Security Training And Awareness
- BUL-999.16 Responsible Use Policy (RUP) for District Computer and Network Systems
- BUL-114700.1 Access to Critical Information Systems
- BUL-050298.1 Fingerprinting Requirements and Procedures
- BUL-3872.1 Fingerprinting and Criminal Background Compliance for Contractors
- BUL-2424.4 Website Development and Management
- BUL-101556.0 Information Security Policy

PR.AT-02 Individuals in specialized roles are provided with awareness and training so that
they possess the knowledge and skills to perform relevant tasks with cybersecurity
risks in mind
- BUL-079114.1 Information Security Training And Awareness
- BUL-999.16 Responsible Use Policy (RUP) for District Computer and Network Systems
- BUL-114700.1 Access to Critical Information Systems
- BUL-050298.1 Fingerprinting Requirements and Procedures
- BUL-3872.1 Fingerprinting and Criminal Background Compliance for Contractors
- BUL-2424.4 Website Development and Management

## 15


- BUL-101556.0 Information Security Policy

Protect: Data Security (PR.DS)


PR.DS-01 The confidentiality, integrity, and availability of data-at-rest are protected
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-K-24.1 LAUSD Firewall Policy
- BUL-101556.0 Information Security Policy

PR.DS-02 The confidentiality, integrity, and availability of data-in-transit are protected
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-K-24.1 LAUSD Firewall Policy
- BUL-101556.0 Information Security Policy

PR.DS-03-09 Withdrawn NIST CSF 2.0

PR.DS-10 The confidentiality, integrity, and availability of data-in-use are protected
- BUL-6916.1 Data Destruction and Disposal
- BUL-5242.1 Web Content Filtering Policy

PR.DS-11 Backups of data are created, protected, maintained, and tested
- BUL-6916.1 Data Destruction and Disposal
- DR/BC Test Plan (Contact GRC for Access)
- BUL-5242.1 Web Content Filtering Policy
- BUL-K-24.1 LAUSD Firewall Policy

Protect: Platform Security (PR.PS)


PR.PS-01 Configuration management practices are established and applied
- BUL-106900.1 Change Management for Critical Information Systems (2)
- BUL-2424.4 Website Development and Management
- BUL-K-24.1 LAUSD Firewall Policy


## 16



PR.PS-02 Software is maintained, replaced, and removed commensurate with risk
- BUL-106900.1 Change Management for Critical Information Systems (2)
- Bul-716.1 Compliance with the 1976 US Copyright Law-Computer Software


PR.PS-03 Hardware is maintained, replaced, and removed commensurate with risk
- BUL-106900.1 Change Management for Critical Information Systems (2)
- BUL-114700.1 Access to Critical Information Systems

PR.PS-04 Log records are generated and made available for continuous monitoring
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-114700.1 Access to Critical Information Systems
- BUL-5242.1 Web Content Filtering Policy
- BUL-K-24.1 LAUSD Firewall Policy

PR.PS-05 Installation and execution of unauthorized software are prevented
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-5242.1 Web Content Filtering Policy
- BUL-2424.4 Website Development and Management
- BUL-K-24.1 LAUSD Firewall Policy

PR.PS-06 Secure software development practices are integrated, and their performance is
monitored throughout the software development life cycle
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- Bul-716.1 Compliance with the 1976 US Copyright Law-Computer Software

## 17


Protect: Technology Infrastructure Resilience (PR.IR)


PR.IR-01 Networks and environments are protected from unauthorized logical access
and usage
- BUL-114700.1 Access to Critical Information Systems
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-1597.0 Acceptable Use Policy for ITD Virtual Private Network (VPN) Services
- BUL-5242.1 Web Content Filtering Policy
- BUL-K-24.1 LAUSD Firewall Policy

PR.IR-02 The organization's technology assets are protected from environmental threats
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-6916.1 Data Destruction and Disposal
- BUL-5242.1 Web Content Filtering Policy
- BUL-K-24.1 LAUSD Firewall Policy

PR.IR-03 Mechanisms are implemented to achieve resilience requirements in normal and
adverse situations
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information
- BUL-5242.1 Web Content Filtering Policy
- BUL-K-24.1 LAUSD Firewall Policy

PR.IR-04 Adequate resource capacity to ensure availability is maintained
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information

## 18


## NIST FUNCTION:
## Detect
Detect: Adverse Event Analysis (DE.AE)

This section deals with how various District teams find and analyze possible cybersecurity attacks and
compromises. DETECT enables timely discovery and analysis of anomalies, indicators of compromise
(IOC), and other potentially adverse cybersecurity events that may indicate that cybersecurity attacks
and incidents are occurring. Links to District Bulletins and Standard Operating Procedures (SOPs) are
provided.

DE.AE-01 Withdrawn from NIST CSF 2.0

DE.AE-02 Potentially adverse events are analyzed to better understand associated activities
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-129101.1 Vulnerability Management Policy
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information

DE.AE-03 Information is correlated from multiple sources
- BUL-129101.1 Vulnerability Management Policy
- REF-3757.0 Description of Security Standards for Networked Computer Systems Housing
## Confidential Information

DE.AE-04 The estimated impact and scope of adverse events are understood
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

DE.AE-05 Withdrawn from NIST CSF 2.0

DE.AE-06 Information on adverse events is provided to authorized staff and tools
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-101556.0 Information Security Policy



DE.AE-07 Cyber threat intelligence and other contextual information are integrated into the



analysis
- Incident Response Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy

DE.AE-08 Incidents are declared when adverse events meet the defined incident criteria
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-101556.0 Information Security Policy

Detect: Continuous Monitoring (DE.CM)


DE.CM-01 Networks and network services are monitored to find potentially adverse events
- BUL-129101.1 Vulnerability Management Policy

DE.CM-02 The physical environment is monitored to find potentially adverse events
- BUL-129101.1 Vulnerability Management Policy

DE.CM-03 Personnel activity and technology usage are monitored to find potentially
adverse events
- BUL-129101.1 Vulnerability Management Policy

DE.CM-04-05   Withdrawn from NIST CSF 2.0

DE.CM-06 External service provider activities and services are monitored to find potentially
adverse events
- BUL-129101.1 Vulnerability Management Policy

DE.CM-07-08 Withdrawn NIST CSF 2.0

DE.CM-09 Computing hardware and software, runtime environments, and their data are
monitored to find potentially adverse events
- BUL-129101.1 Vulnerability Management Policy



## 21



## NIST FUNCTION:
## Respond
Respond: Incident Management (RS.MA)



This section highlights how the District responds regarding a detected cybersecurity incident. RESPOND
supports the ability to contain the impact of cybersecurity incidents. Outcomes within this Function
cover incident management, analysis, mitigation, reporting, and communication. Links to District
Bulletins and Standard Operating Procedures (SOPs) are provided.

RS.MA-01 The incident response plan is executed in coordination with relevant third parties
once an incident is declared
## • Business Continuity
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.MA-02 Incident reports are triaged and validated
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.MA-03 Incidents are categorized and prioritized
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.MA-04 Incidents are escalated or elevated as needed
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.MA-05 The criteria for initiating incident recovery are applied
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

## 22


Respond: Incident Response Reporting and Communication (RS.CO)


RS.CO-01 Withdrawn NIST CSF 2.0

RS.CO-02 Internal and external stakeholders are notified of incidents
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.CO-03 Information is shared with designated internal and external stakeholders
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

Respond: Incident Analysis (RS.AN)


RS.AN-01 Withdrawn NIST CSF 2.0

RS.AN-02 Withdrawn NIST CSF 2.0

RS.AN-03 Analysis is performed to establish what has taken place during an incident and the
root cause of the incident
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.AN-04 Withdrawn NIST CSF 2.0

RS.AN-05 Withdrawn NIST CSF 2.0

RS.AN-06 Actions performed during an investigation are recorded, and the records' integrity
and provenance are preserved
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.AN-07 Incident data and metadata are collected, and their integrity and provenance are
reserved
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.AN-08 An incident's magnitude is estimated and validated
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)


## 23



Respond: Incident Mitigation (RS.MI)


RS.MI-01 Incidents are contained
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)

RS.MI-02 Incidents are eradicated
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)



## NIST FUNCTION:
## Recover
Recover: Incident Recovery Plan Execution (RC.RP)

This section addresses how the District restores assets and operations that were impacted by a
cybersecurity incident. RECOVER supports timely restoration of normal operations to reduce the impact
of cybersecurity incidents and enable appropriate communication during recovery efforts. Links to
District Bulletins and Standard Operating Procedures (SOPs) are provided.

RC.RP-01 The recovery portion of the incident response plan is executed once initiated from
the incident response process
- Business Continuity Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information

RC.RP-02 Recovery actions are selected, scoped, prioritized, and performed
- Business Continuity Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information

RC.RP-03 The integrity of backups and other restoration assets is verified before using them
for restoration
- Business Continuity Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information





## 25


RC.RP-04 Critical mission functions and cybersecurity risk management are considered to
establish post-incident operational norms
- Business Continuity Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information

RC.RP-05 The integrity of restored assets is verified, systems and services are restored, and
normal operating status is confirmed
- Business Continuity Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information

RC.RP-06 The end of incident recovery is declared based on criteria, and incident-related
documentation is completed
- Business Continuity Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information

Recover: Incident Recovery Communication (RC.CO)


RC.CO-01 02 Withdrawn NIST CSF 2.0

RC.CO-03 Recovery activities and progress in restoring operational capabilities are
communicated to designated internal and external stakeholders
- Business Continuity Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information








RC.CO-04 Public updates on incident recovery are shared using approved methods and
messaging
- Business Continuity Plan (Contact GRC for Access)
- BUL-157711 Incident Management Policy
- Incident Response Plan (Contact GRC for Access)
- BUL-1553 Security Standards For Networked Computer Systems Housing Confidential
## Information

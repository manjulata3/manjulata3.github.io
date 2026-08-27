#!/usr/bin/env python3
"""Generate ManjuLata_Singh.pdf from resume content using ReportLab."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUTPUT = "resume.pdf"

SKILLS = [
    ("Test Automation", "Selenium WebDriver, Cucumber (BDD), JBehave, Ready API, SoapUI, Parasoft, Appium, HP QTP"),
    ("Performance & Security", "Rational Performance Test (RPT), JMeter, LoadRunner, HCL AppScan, Ready API endpoint security"),
    ("Accessibility (Section 508)", "SortSite, Lighthouse, Dragon NaturallySpeaking, WCAG validation"),
    ("Mobile Testing", "Appium (Android/iOS), Calabash-Android, Android SDK, emulators, simulators, real devices"),
    ("Languages & Scripting", "Java, Groovy, Ruby, Gherkin, JavaScript, VBScript, SQL, PL/SQL, HTML"),
    ("CI/CD & Build", "Jenkins, Maven, Git, SVN, JUnit, TestNG"),
    ("Test & Project Management", "JIRA, Rally (CA Agile Central), ALM / Quality Center, RTM, Smart Test Manager"),
    ("Databases & Monitoring", "Oracle 9i/10g, Postgres, Sybase, SQL Server, Elasticsearch, Kibana (ELK)"),
    ("AI-Assisted Engineering", "Amazon Q for Selenium automation authoring and code productivity"),
]

JOBS = [
    {
        "title": "QA Lead / Business Analyst / Test Coordinator",
        "dates": "Mar 2024 – Jul 2025",
        "org": "National Science Foundation (PES) — Ashburn, VA",
        "bullets": [
            "Led end-to-end testing and business requirement alignment across NSF applications and third-party vendor systems, serving as the single point of accountability for release quality.",
            "Coordinated daily with vendor application teams, cross-functional groups, and client stakeholders on integration, API, performance, service recovery, and security validation.",
            "Identified impacted systems for each release and convened the owning teams so integration testing covered every interface collectively rather than in isolated silos.",
            "Drove performance testing readiness — aligning stakeholders, engaging monitoring teams, and confirming environments and prod-like data were in place before load and stress runs.",
            "Designed and executed manual and automated suites using Selenium, Ready API, Rational Performance Test, and Jenkins, improving coverage and cycle efficiency across releases.",
            "Owned defect triage and troubleshooting, coordinating resolution across application, infrastructure, and testing teams.",
            "Produced key release artifacts: UAT packages, ITHC briefs, DIS testing summaries, and Release Readiness decks.",
            "Facilitated UAT/ITHC sessions, managed client validation, and ensured compliance with federal release standards.",
            "Supported release-night validation and post-deployment production checks.",
        ],
    },
    {
        "title": "Software Engineer — QA",
        "dates": "Oct 2019 – Feb 2024",
        "org": "National Science Foundation (Research.gov / FastLane)",
        "bullets": [
            "Partnered with business analysts and developers to review requirements, designs, and test plans, providing effort estimates and consolidated test reports.",
            "Executed functional, regression, integration, cross-browser, performance, security, and Section 508 compliance testing.",
            "Automated regression coverage with JBehave, Selenium, and Jenkins; monitored and maintained the automation suite on a daily schedule.",
            "Recorded performance scripts and captured response-time baselines using RPT; ran security scans with HCL AppScan and Ready API endpoint testing.",
            "Built and maintained the requirements traceability matrix mapping user stories to test cases and defects.",
            "Led integration testing efforts, coordinated participating teams, and onboarded new QA members.",
            "Tracked and remediated accessibility findings using SortSite; supported client UAT and defect reporting.",
        ],
    },
    {
        "title": "QA Analyst",
        "dates": "Oct 2018 – Oct 2019",
        "org": "USPTO — Pre-Exam Next Gen",
        "bullets": [
            "Analyzed requirements and authored manual and automated test cases using Java, Selenium, Groovy, Cucumber, Ready API, and Maven, integrated into Jenkins.",
            "Prepared test plans with documented risks and mitigation strategies; maintained traceability from requirement to test case to defect.",
            "Participated in daily scrums, sprint planning, and retrospectives, collaborating with developers and analysts to define system capabilities and interfaces.",
            "Coordinated web component deployments, maintained support documentation, and troubleshot production issues.",
            "Reported test progress, coverage, and defect metrics to project leadership.",
        ],
    },
    {
        "title": "Automation QA Engineer",
        "dates": "May 2017 – Sep 2018",
        "org": "Comcast Cable Communications — Sales Portal",
        "bullets": [
            "Developed and executed automation scripts in Java, Groovy, and Cucumber, orchestrated through Jenkins.",
            "Defined the QA strategy aligned to business goals and documented QA processes for the program.",
            "Built tooling for SOAP XML validation and supported service migration from SOAP to REST.",
            "Developed Selenium scripts for GUI testing and delivered customized client-facing reports.",
            "Managed suite execution, defect tracking, and reporting using Parasoft, SoapUI, and Kibana (ELK).",
        ],
    },
    {
        "title": "Programmer Analyst",
        "dates": "May 2016 – Mar 2017",
        "org": "HCL America — Smart City (City of Boston), Palo Alto & PSM",
        "bullets": [
            "Built an automation framework from scratch in Selenium for web application testing.",
            "Supported Verizon IoT device testing, validating functionality across devices and platforms.",
            "Engaged directly in client discussions to clarify requirements, operating as a hybrid BA/QA.",
            "Analyzed specifications for manual and automated testing of web applications and REST APIs.",
            "Authored test plans covering dependencies, risks, and mitigation; ensured full traceability of requirements to results.",
            "Mentored new team members and delivered training on testing processes.",
        ],
    },
    {
        "title": "Programmer Analyst",
        "dates": "Jan 2016 – May 2016",
        "org": "Wenova Inc. — Dial Easy (St. Louis, MO)",
        "bullets": [
            "Analyzed requirements and supported development of web and mobile applications.",
            "Designed test strategies and evaluated tooling options for the engagement.",
            "Wrote automated scripts using Selenium WebDriver within a hybrid framework.",
            "Tested mobile applications with Calabash and Appium; generated execution reports via Calabash-Android and Cucumber.",
        ],
    },
    {
        "title": "QA Analyst / Mobile Automation Tester",
        "dates": "Jan 2014 – Dec 2014",
        "org": "British Sky Broadcasting (BSkyB) — Scotland",
        "bullets": [
            "Executed mobile automation and functional testing for broadcast platform releases.",
        ],
    },
    {
        "title": "QA Engineer",
        "dates": "Sep 2010 – Dec 2013",
        "org": "Tata Teleservices Limited — IT S&C Testing, India",
        "bullets": [
            "Delivered functional and regression testing across telecom IT systems in an Agile delivery model.",
        ],
    },
]


def build_styles():
    styles = getSampleStyleSheet()
    accent = colors.HexColor("#1e4d8c")
    muted = colors.HexColor("#4a5568")

    styles.add(
        ParagraphStyle(
            name="ResumeName",
            parent=styles["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=18,
            textColor=accent,
            alignment=TA_CENTER,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ResumeTitle",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=muted,
            alignment=TA_CENTER,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ResumeContact",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9,
            textColor=muted,
            alignment=TA_CENTER,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SectionHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10,
            textColor=accent,
            spaceBefore=8,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="Body",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SkillLabel",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9,
            leading=11,
        )
    )
    styles.add(
        ParagraphStyle(
            name="SkillValue",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11,
            textColor=muted,
        )
    )
    styles.add(
        ParagraphStyle(
            name="JobTitle",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=12,
        )
    )
    styles.add(
        ParagraphStyle(
            name="JobDates",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9,
            textColor=muted,
            alignment=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="JobOrg",
            parent=styles["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9,
            textColor=muted,
            spaceAfter=2,
        )
    )
    styles.add(
        ParagraphStyle(
            name="ResumeBullet",
            parent=styles["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11,
            leftIndent=12,
            bulletIndent=0,
            spaceAfter=2,
        )
    )
    return styles


def section_rule():
    return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#d0d7e2"), spaceBefore=0, spaceAfter=4)


def build_pdf(path: str):
    styles = build_styles()
    doc = SimpleDocTemplate(
        path,
        pagesize=letter,
        leftMargin=0.6 * inch,
        rightMargin=0.6 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
        title="Manju Lata Singh — Resume",
        author="Manju Lata Singh",
    )

    story = [
        Paragraph("Manju Lata Singh", styles["ResumeName"]),
        Paragraph("QA Lead | Business Analyst | Test Automation Engineer", styles["ResumeTitle"]),
        Paragraph(
            "Ashburn, VA 20147 · manjulata.singh3@gmail.com · linkedin.com/in/manjulatasingh · manjulatasingh.com",
            styles["ResumeContact"],
        ),
        HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#1e4d8c"), spaceAfter=8),
        Paragraph("PROFESSIONAL SUMMARY", styles["SectionHeading"]),
        section_rule(),
        Paragraph(
            "QA and test engineering professional with 12+ years delivering functional, API, performance, security, "
            "and Section 508 accessibility testing for federal and enterprise programs. Most recently served in a dual "
            "QA Lead / Business Analyst capacity at the National Science Foundation, coordinating integration and "
            "release validation across internal teams and third-party vendors. Builds and maintains automation suites "
            "in Selenium, Cucumber, and Ready API wired into Jenkins, and translates business requirements into "
            "traceable test strategies from user story through UAT sign-off.",
            styles["Body"],
        ),
        Paragraph("CORE COMPETENCIES", styles["SectionHeading"]),
        section_rule(),
    ]

    skill_rows = [[Paragraph(label, styles["SkillLabel"]), Paragraph(value, styles["SkillValue"])] for label, value in SKILLS]
    skill_table = Table(skill_rows, colWidths=[1.75 * inch, 4.55 * inch])
    skill_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(skill_table)
    story.append(Spacer(1, 4))
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["SectionHeading"]))
    story.append(section_rule())

    for job in JOBS:
        header = Table(
            [
                [
                    Paragraph(job["title"], styles["JobTitle"]),
                    Paragraph(job["dates"], styles["JobDates"]),
                ]
            ],
            colWidths=[4.8 * inch, 1.5 * inch],
        )
        header.setStyle(
            TableStyle(
                [
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]
            )
        )
        story.append(header)
        story.append(Paragraph(job["org"], styles["JobOrg"]))
        bullets = ListFlowable(
            [ListItem(Paragraph(b, styles["ResumeBullet"]), leftIndent=10) for b in job["bullets"]],
            bulletType="bullet",
            start="•",
            leftIndent=12,
        )
        story.append(bullets)
        story.append(Spacer(1, 5))

    story.append(Paragraph("EDUCATION", styles["SectionHeading"]))
    story.append(section_rule())
    story.append(Paragraph("<b>Bachelor of Technology, Information Technology</b> — India", styles["Body"]))

    doc.build(story)


if __name__ == "__main__":
    build_pdf(OUTPUT)
    print(f"Wrote {OUTPUT}")

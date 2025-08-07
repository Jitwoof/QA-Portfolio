
# 📂 estiem\_registration\_qa

> **Title:** Optimizing Event Registration for ESTIEM  
> **Role:** QA & Tech Coordinator  
> **Period:** June 2023 – December 2024  
> **Team:** International Student Tech Committee (30+ people)

---

## Introduction

In 2023, as part of my work at **ESTIEM** (European Students of Industrial Engineering and Management), I led a mini QA initiative to enhance the quality and usability of registration forms and event landing pages for international student events. I treated it with a product mindset — focusing on **quality assurance**, **user experience**, and **data accuracy**.

---

##  Problem

There were some issues:

* Broken fields in registration forms
* Missing validations (users submitted empty forms)
* Confusing UI / unclear steps
* Low form completion rate
* Inconsistent data for internal use

Our goal was to ensure that event registration forms and landing pages work flawlessly across devices and deliver clean, complete data to event organizers.

---

## My QA Workflow

### 1. Requirements Analysis

* Defined business requirements with stakeholders (form purpose, target users, expected data)
* Identified mandatory vs optional fields, expected field formats

### 2. Test Design

* Created a **test checklist** (cross-browser, mobile/desktop, negative/positive inputs)
* Designed **test cases** with clear test data, expected results, edge cases

### 3. Test Execution

* Tested forms on **mobile** and **desktop** across Chrome, Safari, Firefox
* Used boundary values and invalid formats to check validation
* Tested usability and flow with real users (UX review with 5 international students)

### 4. Bug Reporting

* Logged bugs with severity, reproducibility, screenshots and clear steps
* Example bugs:

  * Form accepted empty email field (Major)
  * Dropdown didn’t render on Safari (Minor)
  * Broken redirect after submission (Critical)

### 5. Improvements & Iteration

* Collaborated with content and dev teams to fix UX issues
* Re-tested every version (regression testing)
* Integrated Google Forms with Notion and Trello for better internal data workflow

---

## Result

| Metric                        | Before  | After       |
| ----------------------------- | ------- | ----------- |
| Form Completion Rate          | 61%     | **92%**     |
| Incorrect Submissions         | 27%     | **4%**      |
| Participant Satisfaction (UX) | 3.5 / 5 | **4.8 / 5** |
| Bugs Detected & Fixed         | –       | **12**     |

---

## 📄 Included Files

* `test_strategy.md` – general testing principles and goals
* `test_plan.md` – detailed plan and testing schedule
* `test_scenarios.md` – sample scenarios for mobile/desktop testing
* `test_cases.md` – well-structured QA cases
* `checklist_registration_form.xlsx` – practical checklist used in manual testing
* `bug_reports.md` – logged issues with reproduction steps and priority
* `ux_review_summary.pdf` – key usability findings from live testing sessions
* `screenshots/` – real test evidence and results

---

## 🌱 Why It Matters

I demonstrated how a QA mindset can:

* Improve user experience
* Prevent data loss
* Strengthen team collaboration
* Reduce technical support issues

This project helped me develop a structured, analytical approach to quality — from requirement analysis to final regression testing.

---

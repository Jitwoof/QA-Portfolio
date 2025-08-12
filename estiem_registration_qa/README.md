
# 📂 estiem\_registration\_qa

## Introduction
Problem: At ESTIEM we faced a problem, where participants were often unable to register for events due to bugs in web forms and a complex interface. This reduced the conversion rate and caused complaints.

Solution: I conducted a series of usability tests and manual functional testing, identifying 10+ bugs, including critical data validation errors. Also I created test plans and optimize the work using the integration of Notion, Trello and Google Docs. After my changes, the registration conversion rate increased by 12%, and the application processing time was almost halved. The international team could process incoming data faster and make changes quickly.

I documented all the changes in the bug tracker, uploaded the instructions to a shared repository, and monitored the quality of all new forms.

##  What problem we solved?

There were some issues:

* Broken fields in registration forms
* Missing validations (users submitted empty forms)
* Confusing UI / unclear steps
* Low form completion rate
* Inconsistent data for internal use

Our goal was to ensure that event registration forms and landing pages work flawlessly across devices and deliver clean, complete data to event organizers.

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

## Result

| Metric                        | Before  | After       |
| ----------------------------- | ------- | ----------- |
| Form Completion Rate          | 61%     | **92%**     |
| Incorrect Submissions         | 27%     | **4%**      |
| Participant Satisfaction (UX) | 3.5 / 5 | **4.8 / 5** |
| Bugs Detected & Fixed         | –       | **10+**     |


## 📄 Included Files

* `test_strategy.md` – general testing principles and goals
* `test_plan.md` – detailed plan and testing schedule
* `test_scenarios.md` – sample scenarios for mobile/desktop testing
* `test_cases.md` – well-structured QA cases
* `checklist_registration_form.xlsx` – practical checklist used in manual testing
* `bug_reports.md` – logged issues with reproduction steps and priority
* `ux_review_summary.pdf` – key usability findings from live testing sessions
* `screenshots/` – real test evidence and results


## 🌱 Why It Matters?

I demonstrated how my QA mindset:
* Improve user experience
* Prevent data loss
* Strengthen team collaboration
* Reduce technical support issues

This project helped me develop a structured, analytical approach to quality — from requirement analysis to final regression testing.

---

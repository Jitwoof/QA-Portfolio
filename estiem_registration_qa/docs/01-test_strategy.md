# Test Plan — ESTIEM Registration Portal

## INTRODUCTION
This document describes the test plan for the ESTIEM Registration Portal, which is used by students and organizers to register for events, manage profiles, and communicate with the international team.  
The main objective is to ensure stability, usability, and data consistency across the registration process.

---

## 1. OBJECTIVES
- Verify functional correctness of the registration and login modules.  
- Validate usability of UI/UX for end-users.  
- Ensure that data is stored consistently in the database.  
- Identify defects early and track them until resolution.  
- Provide test coverage for positive, negative, and edge scenarios.  

---

## 2. SCOPE
**In scope**:  
- Registration form (input validation, mandatory fields, duplicate handling).  
- Login/authentication flow.  
- Email confirmation.  
- Database record creation and updates.  
- UI/UX behavior across different browsers.  

**Out of scope**:  
- Payment systems (not integrated in current release).  
- External 3rd-party services not owned by ESTIEM.  

---

## 3. ASSUMPTIONS / RISKS  

### 3.1 ASSUMPTIONS
- Requirements are stable and do not change during the test cycle.  
- Test environment reflects production environment.  
- Test data can be freely inserted and cleared from the database.  

### 3.2 RISKS
- High traffic during event registration may cause performance issues.  
- Lack of automated regression coverage may delay release cycles.  
- Dependencies on external mail servers may affect confirmation testing.  

---

## 4. TEST APPROACH
- Manual functional testing (UI, API, forms validation).  
- Negative and boundary testing for form inputs.  
- Cross-browser testing (Chrome, Firefox, Safari).  
- Database validation using SQL queries.  
- Smoke & regression cycles before releases.  

### 4.1 TEST AUTOMATION
- Basic automation with **Pytest** considered for regression (login + registration happy path).  
- Automation scope: API endpoints and form submission flows.  

---

## 5. TEST ENVIRONMENT
- **Web app**: ESTIEM Registration Portal (staging + production).  
- **Browsers**: Chrome (latest), Firefox (latest), Safari.  
- **Database**: PostgreSQL (staging).  
- **Tools**: Jira (bug tracking), Google Sheets/Excel (scenarios), Postman (API testing).  

---

## 6. MILESTONES / DELIVERABLES  

### 6.1 TEST SCHEDULE
- Week 1 — Review requirements, prepare scenarios.  
- Week 2 — Execute functional tests, log defects.  
- Week 3 — Regression cycle, verify fixes.  
- Week 4 — Final acceptance testing.  

### 6.2 DELIVERABLES
- **registration_form_test-scenarios.xlsx** — functional scenarios for registration module.  
- Test cases (Markdown or Excel) derived from scenarios.  
- Bug reports in Jira.  
- Final Test Report (summary of defects, pass/fail rate, release recommendation).  

---

## REFERENCES
- Test Strategy — ESTIEM QA Project  
- Test Scenarios — [registration_form_test-scenarios.xlsx](./registration_form_test-scenarios.xlsx)  

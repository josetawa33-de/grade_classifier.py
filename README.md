# Week 4 Assignment: Grades, Eligibility & Smart Decisions

This repository contains three Python programs:

- **grade_classifier.py** — Classifies scores into grades A–F with validation.  
- **eligibility_checker.py** — Determines coding club eligibility using age and parental consent, now refactored to use compound boolean operators (`and`, `or`) for clearer logic.  
- **atm_menu.py** — Simulates an ATM with PIN check and withdrawal logic.

### Reflection
The most challenging part was refining `eligibility_checker.py`. At first, I relied on nested if‑else blocks, but after feedback I refactored it to use compound boolean operators. This made the code shorter, easier to read, and more efficient. I also learned that using `elif` is better than separate `if` statements when conditions are mutually exclusive, since it ensures only one branch executes and avoids redundant checks.

# L6_L7_48 — Daycare Fees

Lab 6: Code and Branch Coverage

## About

A small Python module that works out extra-hours fees by age group, hours and sibling discount, checks whether an enrolment is allowed and reports child pickup status.

## Files

| File | Description |
|------|-------------|
| `daycare_fees.py` | The module under test |
| `test_daycare_fees.py` | Starter test file |

Keep all your Lab 6 work in this `LAB6` folder. Lab 7 will be added to this repo later.

Refer to the lab handout for instructions.

## Coverage results

Run these commands from the `Lab 6` directory:

```bash
python3 -m coverage run --source=. -m pytest CodeCoverageTest_daycare_fees.py
python3 -m coverage report -m --include=daycare_fees.py
```

The line-coverage test suite reports 100% coverage for `daycare_fees.py`.

```bash
python3 -m coverage erase
python3 -m coverage run --branch --source=. -m pytest BranchCoverageTest_daycare_fees.py
python3 -m coverage report -m --include=daycare_fees.py
```

The branch-coverage test suite reports 100% statement coverage and 100% branch
coverage for `daycare_fees.py`.

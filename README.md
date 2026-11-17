# Snowflake Warehouse Workload Review

Analyzes representative query-history exports to spot slow queries, high-credit workloads, and repeat offenders.  
Provides Snowflake SQL examples for query-history inspection and targeted performance investigation.

## Problem

Warehouse teams need defensible priorities for tuning rather than optimizing queries at random.

## Solution and design

Summarize execution time and cloud-credit estimates by query fingerprint, then rank high-cost patterns.

**Stack:** Snowflake SQL, Python, query tuning, FinOps

## Quick start

Requires Python 3.11+ (standard library only for the local demo).

```bash
python main.py
python -m unittest discover -s tests -v
```

A GitHub Actions workflow runs the same tests on pushes and pull requests.

## Project layout

- `main.py`: core processing and a small command-line demonstration
- `data/`, `seeds/`, `models/`, `sql/`, `infra/`, `dags/` or `powerbi/`: included only where relevant
- `tests/`: fixture-based expected-value and repeatability checks

## Engineering decisions

- Narrow scope, realistic field names, and synthetic reproducible inputs
- No credentials, customer records, patient data, API tokens, or paid cloud resources
- Visible business logic and deterministic fixtures rather than screenshots of unverifiable dashboards

## Limits and next iteration

Uses synthetic query history; the SQL is a reference query and does not connect to or modify a Snowflake account.

A production hardening path would add larger-scale fixtures, alerting, operational runbooks, robust error handling, and integration tests against the real deployment target.

## Portfolio integrity

This is an independently reproducible **portfolio demonstration**, not a claim that these files are employer code or that a cloud workload has been deployed. The fixture data is synthetic.

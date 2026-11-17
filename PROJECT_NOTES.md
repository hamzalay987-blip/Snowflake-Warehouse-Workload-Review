# Project notes: Snowflake Warehouse Workload Review

**Business problem:** Warehouse teams need defensible priorities for tuning rather than optimizing queries at random.

**Design:** Summarize execution time and cloud-credit estimates by query fingerprint, then rank high-cost patterns.

**Interview discussion:** Explain schema assumptions, late data/duplicate behavior, controls, expected tradeoffs, and what would change at enterprise scale.

**Suggested next feature:** Add sample-sized integration tests or a docker-compose service when the implementation is ready.

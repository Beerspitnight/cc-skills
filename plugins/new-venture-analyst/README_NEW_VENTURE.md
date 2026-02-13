

# New Venture Analyst Skill

This skill transforms Claude into a strategic business analyst capable of critiquing business plans, modeling financial scenarios, and evaluating Go-To-Market (GTM) strategies.

## Capabilities

*   **Financial Modeling**: Uses a deterministic Python script (`model_financials.py`) to generate Pessimistic, Realistic, and Optimistic 12-month projections based on user assumptions.
*   **Strategic Critique**: Validates unit economics (LTV:CAC, Payback Period) and flags "death valley" metrics.
*   **GTM Analysis**: Evaluates channel-market fit based on ARPU and target audience.
*   **Risk Assessment**: Identifies specific execution and market risks with mitigation strategies.

## File Structure

```text
new-venture-analyst/
├── SKILL.md                     # Core agent instructions and workflow
├── README.md                    # This file
├── scripts/
│   └── model_financials.py      # Python script for 12-month projections
└── references/
    └── evaluation_guide.md      # Knowledge base for metrics and benchmarks
```

## Usage

### Prerequisites
*   **Python 3.x**: Required to run the financial modeling script.

### Triggering the Skill
The skill is designed to be triggered when a user presents a business idea, pitch deck, or set of assumptions.

**Example Prompt:**
> "Analyze this business plan for a subscription coffee service. We plan to charge $20/mo, expect $15 CAC via Instagram ads, and have $5 COGS."

### Automatic Script Execution
The skill automatically extracts variables from the prompt and executes `model_financials.py` with the following arguments:

*   `--start_users`: Initial user count (default: 0)
*   `--growth_rate`: Monthly growth percentage (e.g., 0.10)
*   `--arpu`: Average Revenue Per User
*   `--churn`: Monthly churn rate (decimal)
*   `--cac`: Customer Acquisition Cost
*   `--cogs`: Cost of Goods Sold per unit
*   `--fixed_costs`: Monthly operational costs (hosting, salaries, etc.)

## Customization

To adjust the "stress test" parameters for the Pessimistic/Optimistic scenarios, edit the multipliers in `scripts/model_financials.py`:

```python
# Current defaults:
# Pessimistic: 0.5x Growth
# Realistic:   1.0x Growth
# Optimistic:  1.5x Growth
```
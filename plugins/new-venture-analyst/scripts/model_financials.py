### 3. Create `new-venture-analyst/scripts/model_financials.py`

This script handles the heavy lifting of calculating the 3 scenarios so the LLM doesn't halllucinate the math.

```python
import argparse
import sys

def calculate_scenario(name, start_users, growth_rate, arpu, churn, cac, cogs, fixed_costs, multiplier):
    """
    Calculates a 12-month projection for a specific scenario multiplier.
    multiplier applies to growth (x) and churn (1/x).
    """
    # Adjust assumptions based on scenario
    effective_growth = growth_rate * multiplier
    effective_churn = churn * (1 + (1 - multiplier)) # Simple inverse proxy for stress testing
    if effective_churn < 0: effective_churn = 0
    if effective_churn > 1: effective_churn = 1

    total_revenue = 0
    total_profit = 0
    
    # We will output the Month 12 snapshot and the 12-month Total
    
    current_users = start_users
    
    # 12 Month Loop
    for month in range(1, 13):
        # New users
        new_users = int(current_users * effective_growth)
        if month == 1 and start_users == 0: new_users = 1 # Force start if 0
            
        # Churned users
        churned_users = int(current_users * effective_churn)
        
        # Net users
        current_users = current_users + new_users - churned_users
        
        # Financials
        revenue = current_users * arpu
        direct_costs = current_users * cogs
        acq_costs = new_users * cac
        operating_profit = revenue - direct_costs - acq_costs - fixed_costs
        
        total_revenue += revenue
        total_profit += operating_profit

    return {
        "Scenario": name,
        "End Users": int(current_users),
        "Total Revenue": int(total_revenue),
        "Total Profit": int(total_profit),
        "Monthly Burn/Profit (M12)": int(operating_profit)
    }

def main():
    parser = argparse.ArgumentParser(description="Generate 12-month financial scenarios.")
    parser.add_argument("--start_users", type=int, default=0)
    parser.add_argument("--growth_rate", type=float, required=True, help="Decimal format (e.g., 0.10 for 10%)")
    parser.add_argument("--arpu", type=float, required=True)
    parser.add_argument("--churn", type=float, default=0.05)
    parser.add_argument("--cac", type=float, default=0)
    parser.add_argument("--cogs", type=float, default=0)
    parser.add_argument("--fixed_costs", type=float, default=0)

    args = parser.parse_args()

    # Define Scenarios
    # Pessimistic: 50% of target growth
    # Realistic: 100% of target growth
    # Optimistic: 150% of target growth
    
    scenarios = [
        calculate_scenario("Pessimistic", args.start_users, args.growth_rate, args.arpu, args.churn, args.cac, args.cogs, args.fixed_costs, 0.5),
        calculate_scenario("Realistic", args.start_users, args.growth_rate, args.arpu, args.churn, args.cac, args.cogs, args.fixed_costs, 1.0),
        calculate_scenario("Optimistic", args.start_users, args.growth_rate, args.arpu, args.churn, args.cac, args.cogs, args.fixed_costs, 1.5),
    ]

    # Output Markdown Table
    print("| Scenario | Month 12 Users | Total 1st Year Rev | Total 1st Year Profit/Loss | Month 12 Burn/Profit |")
    print("| :--- | :--- | :--- | :--- | :--- |")
    for s in scenarios:
        print(f"| **{s['Scenario']}** | {s['End Users']:,} | ${s['Total Revenue']:,} | ${s['Total Profit']:,} | ${s['Monthly Burn/Profit (M12)']:,} |")
    
    print("\n*Projections generated via deterministic modeling script based on user inputs.*")

if __name__ == "__main__":
    main()
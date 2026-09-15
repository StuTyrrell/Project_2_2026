# EPQ Model: Calculates the optimal batch size for self-manufactured inventory 
# by balancing fixed setup costs against holding costs while accounting for concurrent production and usage.

import math

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    """Calculates optimal production quantity (EPQ)."""
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - (d_rate / p_rate))))

def run_epq_analysis(demand, setup, hold_cost, d_rate, p_rate):
    """Runs full EPQ analysis and prints summary metrics."""
    epq = calculate_epq(demand, setup, hold_cost, d_rate, p_rate)
    runs_per_year = demand / epq
    run_length_days = epq / p_rate
    max_inventory = epq * (1 - (d_rate / p_rate))

    print("=== EPQ ANALYSIS RESULTS ===")
    print(f"Optimal production quantity (EPQ): {round(epq, 2)}")
    print(f"Production runs per year: {round(runs_per_year, 2)}")
    print(f"Length of each run (days): {round(run_length_days, 1)}")
    print(f"Maximum inventory level: {round(max_inventory, 2)}\n")

if __name__ == "__main__":
    # Standard inputs from classwork
    annual_demand = 12000
    setup_cost = 50
    holding_cost = 2
    daily_demand_rate = 40
    daily_production_rate = 100

    run_epq_analysis(annual_demand, setup_cost, holding_cost, daily_demand_rate, daily_production_rate)

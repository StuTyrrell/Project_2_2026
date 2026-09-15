# ABC Inventory Classification Model: Ranks SKUs by cumulative usage value using the Pareto principle
# to segment inventory into Tier A (high value), Tier B (moderate value), and Tier C (low value) control groups.

def assign_tier(cum_pct):
    """Assigns inventory tier based on cumulative percentage thresholds."""
    if cum_pct <= 80:
        return "A"
    elif cum_pct <= 95:
        return "B"
    else:
        return "C"

def classify_inventory(skus):
    """Calculates usage value, cumulative percentage, and assigns ABC tiers."""
    # Step 1: Calculate annual usage value
    for item in skus:
        item["value"] = item["demand"] * item["cost"]

    # Step 2: Sort descending by value
    skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

    # Step 3: Calculate cumulative percentage
    total_value = sum(item["value"] for item in skus_sorted)
    running_total = 0
    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100
        item["tier"] = assign_tier(item["cum_pct"])

    return skus_sorted

if __name__ == "__main__":
    skus = [
        {"sku": "BRK-100", "demand": 2000, "cost": 45},
        {"sku": "GSK-220", "demand": 1500, "cost": 30},
        {"sku": "BLT-010", "demand": 10000, "cost": 2},
        {"sku": "BRG-330", "demand": 800, "cost": 60},
        {"sku": "SEAL-500", "demand": 3000, "cost": 5},
        {"sku": "MTR-700", "demand": 50, "cost": 800},
        {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
        {"sku": "CBL-900", "demand": 400, "cost": 25},
    ]

    classified_skus = classify_inventory(skus)

    print("=== ABC CLASSIFICATION REPORT ===")
    tier_counts = {"A": 0, "B": 0, "C": 0}
    for item in classified_skus:
        tier_counts[item["tier"]] += 1
        print(f"{item['sku']} | Value: R{item['value']:,.2f} | Cum %: {round(item['cum_pct'], 1)}% | Tier: {item['tier']}")

    print("\nTier Breakdown Counter:")
    print(tier_counts)

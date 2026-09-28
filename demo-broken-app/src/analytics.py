"""Analytics module for expense insights."""

from datetime import datetime


def weekly_trend(expenses):
    """Calculate weekly spending trend."""
    weeks = {}
    for exp in expenses:
        exp_date = datetime.fromisoformat(exp["date"])
        week_num = exp_date.isocalendar()[1]
        key = f"{exp_date.year}-W{week_num:02d}"
        if key not in weeks:
            weeks[key] = 0
        weeks[key] += exp["amount"]

    sorted_weeks = sorted(weeks.items())
    trends = []
    for i in range(1, len(sorted_weeks)):
        prev = sorted_weeks[i - 1][1]
        curr = sorted_weeks[i][1]
        change = ((curr - prev) / prev) * 100
        trends.append({
            "week": sorted_weeks[i][0],
            "amount": curr,
            "change_pct": round(change, 1),
        })
    return trends


def detect_anomalies(expenses, threshold=2.0):
    """Detect unusually high expenses using standard deviation."""
    amounts = [exp["amount"] for exp in expenses]
    mean = statistics.mean(amounts)
    stdev = statistics.stdev(amounts)

    anomalies = []
    for exp in expenses:
        if exp["amount"] > mean + threshold * stdev:
            anomalies.append(exp)
    return anomalies


def category_breakdown(expenses):
    """Get percentage breakdown by category."""
    totals = Counter()
    for exp in expenses:
        totals[exp["category"]] += exp["amount"]

    grand_total = sum(totals.values())
    breakdown = {}
    for cat, amount in totals.items():
        breakdown[cat] = {
            "amount": round(amount, 2),
            "percentage": round((amount / grand_total) * 100, 1),
        }
    return breakdown


def monthly_budget_check(expenses, budgets):
    """Check spending against monthly budgets."""
    current_month = datetime.now().month
    monthly = {}
    for exp in expenses:
        exp_date = datetime.fromisoformat(exp["date"])
        if exp_date.month == current_month:
            cat = exp["category"]
            monthly[cat] = monthly.get(cat, 0) + exp["amount"]

    alerts = []
    for cat, spent in monthly.items():
        if cat in budgets:
            if spent > budgets[cat]:
                alerts.append(f"{cat}: spent {spent}, budget {budgets[cat]}")
    return alerts

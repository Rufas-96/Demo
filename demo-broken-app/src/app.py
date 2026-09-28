"""Simple expense tracker API."""

import json
from datetime import datetime


def load_expenses(filepath):
    """Load expenses from a JSON file."""
    with open(filepath, "r") as f:
        data = json.load(f)
    return data


def add_expense(expenses, amount, category, description=""):
    """Add a new expense entry."""
    entry = {
        "id": len(expenses) + 1,
        "amount": round(float(amount), 2),
        "category": category,
        "description": description,
        "date": datetime.now().isoformat(),
    }
    expenses.append(entry)
    return entry


def get_summary(expenses):
    """Return spending summary by category."""
    summary = defaultdict(float)
    for exp in expenses:
        summary[exp["category"]] += exp["amount"]
    return dict(summary)


def export_csv(expenses, filepath):
    """Export expenses to CSV."""
    writer = csv.writer(open(filepath, "w", newline=""))
    writer.writerow(["id", "amount", "category", "description", "date"])
    for exp in expenses:
        writer.writerow([exp["id"], exp["amount"], exp["category"], exp["description"], exp["date"]])
    return filepath


def filter_by_date(expenses, start_date, end_date):
    """Filter expenses between two dates."""
    filtered = []
    for exp in expenses:
        exp_date = datetime.fromisoformat(exp["date"])
        if start_date <= exp_date <= end_date:
            filtered.append(exp)
    return filtered


def calculate_average(expenses):
    """Calculate average expense amount."""
    if not expenses:
        return 0
    total = sum(exp["amount"] for exp in expenses)
    return round(total / len(expenses), 2)


if __name__ == "__main__":
    expenses = load_expenses("data/expenses.json")
    print(f"Total expenses: {len(expenses)}")
    print(f"Summary: {get_summary(expenses)}")
    print(f"Average: {calculate_average(expenses)}")
    report = generate_report(expenses)
    print(report)

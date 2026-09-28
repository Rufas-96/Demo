"""Tests for the expense tracker."""

from src.app import add_expense, calculate_average, get_summary


def test_add_expense():
    expenses = []
    entry = add_expense(expenses, 42.50, "food", "lunch")
    assert entry["amount"] == 42.50
    assert entry["category"] == "food"
    assert len(expenses) == 1


def test_calculate_average():
    expenses = [
        {"amount": 10.0},
        {"amount": 20.0},
        {"amount": 30.0},
    ]
    assert calculate_average(expenses) == 20.0


def test_calculate_average_empty():
    assert calculate_average([]) == 0


def test_get_summary():
    expenses = [
        {"category": "food", "amount": 25.0},
        {"category": "transport", "amount": 15.0},
        {"category": "food", "amount": 10.0},
    ]
    summary = get_summary(expenses)
    assert summary["food"] == 35.0
    assert summary["transport"] == 15.0

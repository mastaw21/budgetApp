"""Core business logic for the budget CLI app."""

from typing import Any, Dict, List


def add_transaction(transactions: List[Dict[str, Any]], transaction: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Add a transaction to the transaction list and return the updated list."""
    required_fields = ["date", "type", "category", "description", "amount", "memo"]
    normalized_transaction = {field: transaction.get(field) for field in required_fields}
    return transactions + [normalized_transaction]


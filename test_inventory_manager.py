
import pytest

from inventory_manager import (
    load_inventory,
    save_inventory,
    find_matching_items,
    remove_item_by_number,
    update_item_quantity,
    validate_new_item,
    calculate_summary,
)


@pytest.fixture
def sample_inventory():
    """Provide sample inventory with multiple categories and low-stock items."""
    return [
        {"name": "Hammer", "category": "Tools", "quantity": 10},
        {"name": "Screwdriver", "category": "Tools", "quantity": 4},
        {"name": "Apple", "category": "Food", "quantity": 5},
        {"name": "Bread", "category": "Food", "quantity": 2},
    ]


@pytest.fixture
def empty_inventory():
    """Provide an empty inventory."""
    return []


# --------------------------------------------------
# File Loading Tests
# --------------------------------------------------

def test_load_valid_inventory(tmp_path):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text(
        "Hammer|Tools|10\nApple|Food|5\n",
        encoding="utf-8"
    )

    expected = [
        {"name": "Hammer", "category": "Tools", "quantity": 10},
        {"name": "Apple", "category": "Food", "quantity": 5},
    ]

    # Act
    result = load_inventory(test_file)

    # Assert
    assert result == expected


def test_load_quantities_as_integers(tmp_path):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text("Hammer|Tools|10\n", encoding="utf-8")

    # Act
    result = load_inventory(test_file)

    # Assert
    assert isinstance(result[0]["quantity"], int)
    assert result[0]["quantity"] == 10


def test_load_ignores_blank_lines(tmp_path):
    # Arrange
    test_file = tmp_path / "inventory.txt"
    test_file.write_text(
        "\nHammer|Tools|10\n\nApple|Food|5\n\n",
        encoding="utf-8"
    )

    # Act
    result = load_inventory(test_file)

    # Assert
    assert len(result) == 2
    assert result[0]["name"] == "Hammer"
    assert result[1]["name"] == "Apple"


def test_load_missing_file_returns_empty_list(tmp_path):
    # Arrange
    test_file = tmp_path / "missing_inventory.txt"

    # Act
    result = load_inventory(test_file)

    # Assert
    assert result == []


# --------------------------------------------------
# File Saving Tests
# --------------------------------------------------

def test_save_multiple_items(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"

    expected = (
        "Hammer|Tools|10\n"
        "Screwdriver|Tools|4\n"
        "Apple|Food|5\n"
        "Bread|Food|2\n"
    )

    # Act
    save_inventory(sample_inventory, test_file)
    result = test_file.read_text(encoding="utf-8")

    # Assert
    assert result == expected


def test_save_empty_inventory(tmp_path, empty_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"

    # Act
    save_inventory(empty_inventory, test_file)

    # Assert
    assert test_file.exists()
    assert test_file.read_text(encoding="utf-8") == ""


def test_save_load_round_trip(tmp_path, sample_inventory):
    # Arrange
    test_file = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, test_file)
    result = load_inventory(test_file)

    # Assert
    assert result == sample_inventory


# --------------------------------------------------
# Search Tests
# --------------------------------------------------

def test_search_exact_match(sample_inventory):
    # Arrange
    search_term = "Hammer"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert len(result) == 1
    assert result[0]["name"] == "Hammer"


def test_search_partial_match(sample_inventory):
    # Arrange
    search_term = "Ham"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert len(result) == 1
    assert result[0]["name"] == "Hammer"


def test_search_ignores_capitalization(sample_inventory):
    # Arrange
    search_term = "HAMMER"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert len(result) == 1
    assert result[0]["name"] == "Hammer"


def test_search_multiple_matches(sample_inventory):
    # Arrange
    search_term = "e"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert len(result) == 4
    assert {item["name"] for item in result} == {
        "Hammer", "Screwdriver", "Apple", "Bread"
    }


def test_search_no_matches(sample_inventory):
    # Arrange
    search_term = "Computer"

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert result == []


@pytest.mark.parametrize(
    "search_term",
    ["", " ", "   "],
    ids=["empty", "one-space", "multiple-spaces"]
)
def test_search_empty_or_whitespace_returns_empty(sample_inventory, search_term):
    # Arrange
    # The search term is supplied by the parameter.

    # Act
    result = find_matching_items(sample_inventory, search_term)

    # Assert
    assert result == []


# --------------------------------------------------
# Remove Item Tests
# --------------------------------------------------

@pytest.mark.parametrize(
    "item_number, expected_removed",
    [
        (1, "Hammer"),
        (2, "Screwdriver"),
        (4, "Bread"),
    ],
    ids=["first-item", "middle-item", "last-item"]
)
def test_remove_item_positions(sample_inventory, item_number, expected_removed):
    # Arrange
    original_length = len(sample_inventory)

    # Act
    removed = remove_item_by_number(sample_inventory, item_number)

    # Assert
    assert removed["name"] == expected_removed
    assert len(sample_inventory) == original_length - 1
    assert all(
        item["name"] != expected_removed
        for item in sample_inventory
    )


@pytest.mark.parametrize(
    "item_number",
    [0, -1, 5, 100],
    ids=["zero", "negative", "one-past-end", "far-past-end"]
)
def test_remove_invalid_item_number(sample_inventory, item_number):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = remove_item_by_number(sample_inventory, item_number)

    # Assert
    assert result is None
    assert sample_inventory == original_inventory


def test_remove_middle_item_updates_inventory(sample_inventory):
    # Arrange
    expected_inventory = [
        {"name": "Hammer", "category": "Tools", "quantity": 10},
        {"name": "Apple", "category": "Food", "quantity": 5},
        {"name": "Bread", "category": "Food", "quantity": 2},
    ]

    # Act
    removed = remove_item_by_number(sample_inventory, 2)

    # Assert
    assert removed["name"] == "Screwdriver"
    assert sample_inventory == expected_inventory


# --------------------------------------------------
# Update Quantity Tests
# --------------------------------------------------

def test_update_valid_quantity(sample_inventory):
    # Arrange
    new_quantity = 15

    # Act
    result = update_item_quantity(sample_inventory, 1, new_quantity)

    # Assert
    assert result is True
    assert sample_inventory[0]["quantity"] == 15


def test_update_quantity_accepts_zero(sample_inventory):
    # Arrange
    new_quantity = 0

    # Act
    result = update_item_quantity(sample_inventory, 1, new_quantity)

    # Assert
    assert result is True
    assert sample_inventory[0]["quantity"] == 0


def test_update_quantity_changes_only_selected_item(sample_inventory):
    # Arrange
    expected_inventory = [
        {"name": "Hammer", "category": "Tools", "quantity": 10},
        {"name": "Screwdriver", "category": "Tools", "quantity": 15},
        {"name": "Apple", "category": "Food", "quantity": 5},
        {"name": "Bread", "category": "Food", "quantity": 2},
    ]

    # Act
    result = update_item_quantity(sample_inventory, 2, 15)

    # Assert
    assert result is True
    assert sample_inventory == expected_inventory


@pytest.mark.parametrize(
    "item_number",
    [0, -1, 5, 100],
    ids=["zero", "negative", "one-past-end", "far-past-end"]
)
def test_update_invalid_item_number(sample_inventory, item_number):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = update_item_quantity(sample_inventory, item_number, 20)

    # Assert
    assert result is False
    assert sample_inventory == original_inventory


def test_update_rejects_negative_quantity(sample_inventory):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = update_item_quantity(sample_inventory, 1, -5)

    # Assert
    assert result is False
    assert sample_inventory == original_inventory


# --------------------------------------------------
# Add Item Validation Tests
# --------------------------------------------------

def test_validate_valid_new_item(sample_inventory):
    # Arrange
    name = "Wrench"
    category = "Tools"
    quantity = 8

    # Act
    result = validate_new_item(sample_inventory, name, category, quantity)

    # Assert
    assert result is True
    assert len(sample_inventory) == 4


@pytest.mark.parametrize(
    "name, category, quantity",
    [
        ("", "Tools", 5),
        ("   ", "Tools", 5),
        ("Wrench", "", 5),
        ("Wrench", "   ", 5),
        ("Bad|Name", "Tools", 5),
        ("Wrench", "Bad|Category", 5),
        ("Wrench", "Tools", -1),
        ("Hammer", "Tools", 5),
        ("hammer", "Tools", 5),
    ],
    ids=[
        "empty-name",
        "whitespace-name",
        "empty-category",
        "whitespace-category",
        "separator-in-name",
        "separator-in-category",
        "negative-quantity",
        "duplicate-name",
        "duplicate-name-different-case",
    ]
)
def test_validate_rejects_invalid_new_items(
    sample_inventory, name, category, quantity
):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = validate_new_item(
        sample_inventory, name, category, quantity
    )

    # Assert
    assert result is False
    assert sample_inventory == original_inventory


@pytest.mark.parametrize(
    "quantity",
    ["five", "5", 5.5, True],
    ids=["text", "numeric-string", "decimal", "boolean"]
)
def test_validate_rejects_non_integer_quantities(sample_inventory, quantity):
    # Arrange
    name = "Wrench"
    category = "Tools"

    # Act
    result = validate_new_item(
        sample_inventory, name, category, quantity
    )

    # Assert
    assert result is False


# --------------------------------------------------
# Summary Tests
# --------------------------------------------------

def test_summary_unique_item_count(sample_inventory):
    # Arrange
    expected_count = 4

    # Act
    result = calculate_summary(sample_inventory)

    # Assert
    assert result["unique_items"] == expected_count


def test_summary_total_quantity(sample_inventory):
    # Arrange
    expected_total = 21

    # Act
    result = calculate_summary(sample_inventory)

    # Assert
    assert result["total_quantity"] == expected_total


def test_summary_low_stock_count(sample_inventory):
    # Arrange
    expected_low_stock = 2

    # Act
    result = calculate_summary(sample_inventory)

    # Assert
    assert result["low_stock_items"] == expected_low_stock


@pytest.mark.parametrize(
    "quantity, expected_low_stock",
    [
        (4, 1),
        (5, 0),
    ],
    ids=["below-low-stock-limit", "at-low-stock-limit"]
)
def test_summary_low_stock_boundary(quantity, expected_low_stock):
    # Arrange
    inventory = [
        {"name": "Test Item", "category": "Test", "quantity": quantity}
    ]

    # Act
    result = calculate_summary(inventory)

    # Assert
    assert result["low_stock_items"] == expected_low_stock


def test_summary_category_counts(sample_inventory):
    # Arrange
    expected_categories = {
        "tools": {"name": "Tools", "count": 2},
        "food": {"name": "Food", "count": 2},
    }

    # Act
    result = calculate_summary(sample_inventory)

    # Assert
    assert result["categories"] == expected_categories


def test_summary_groups_categories_without_case_sensitivity():
    # Arrange
    inventory = [
        {"name": "Hammer", "category": "Tools", "quantity": 10},
        {"name": "Wrench", "category": "tools", "quantity": 5},
    ]

    # Act
    result = calculate_summary(inventory)

    # Assert
    assert result["categories"] == {
        "tools": {"name": "Tools", "count": 2}
    }


def test_summary_empty_inventory(empty_inventory):
    # Arrange
    expected_summary = {
        "unique_items": 0,
        "total_quantity": 0,
        "low_stock_items": 0,
        "categories": {},
    }

    # Act
    result = calculate_summary(empty_inventory)

    # Assert
    assert result == expected_summary

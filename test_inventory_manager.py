import pytest

from inventory_manager import (
    load_inventory,
    save_inventory,
    find_matching_items,
    remove_item_by_number,
    update_item_quantity,
    validate_new_item
)

# --------------------------------------------------
# Fixtures
# --------------------------------------------------

@pytest.fixture
def sample_inventory():
    """Provide reusable sample inventory data."""

    # Arrange
    return [
        {"name": "Hammer", "category": "Tools", "quantity": 10},
        {"name": "Screwdriver", "category": "Tools", "quantity": 4},
        {"name": "Apple", "category": "Food", "quantity": 5},
        {"name": "Bread", "category": "Food", "quantity": 2}
    ]


@pytest.fixture
def empty_inventory():
    """Provide an empty inventory."""

    # Arrange
    return []


# --------------------------------------------------
# File Loading Tests
# --------------------------------------------------

def test_load_valid_inventory(tmp_path):
    # Arrange
    file_path = tmp_path / "inventory.txt"
    file_path.write_text(
        "Hammer|Tools|10\n"
        "Apple|Food|5\n",
        encoding="utf-8"
    )

    expected = [
        {"name": "Hammer", "category": "Tools", "quantity": 10},
        {"name": "Apple", "category": "Food", "quantity": 5}
    ]

    # Act
    inventory = load_inventory(file_path)

    # Assert
    assert inventory == expected


def test_load_quantities_as_integers(tmp_path):
    # Arrange
    file_path = tmp_path / "inventory.txt"
    file_path.write_text("Hammer|Tools|10\n", encoding="utf-8")

    # Act
    inventory = load_inventory(file_path)

    # Assert
    assert isinstance(inventory[0]["quantity"], int)
    assert inventory[0]["quantity"] == 10


def test_load_ignores_blank_lines(tmp_path):
    # Arrange
    file_path = tmp_path / "inventory.txt"
    file_path.write_text(
        "\nHammer|Tools|10\n\nApple|Food|5\n\n",
        encoding="utf-8"
    )

    # Act
    inventory = load_inventory(file_path)

    # Assert
    assert len(inventory) == 2
    assert inventory[0]["name"] == "Hammer"
    assert inventory[1]["name"] == "Apple"


def test_load_missing_file(tmp_path):
    # Arrange
    file_path = tmp_path / "missing.txt"

    # Act
    inventory = load_inventory(file_path)

    # Assert
    assert inventory == []

# --------------------------------------------------
# File Saving Tests
# --------------------------------------------------

def test_save_multiple_items(tmp_path, sample_inventory):
    # Arrange
    file_path = tmp_path / "inventory.txt"

    expected = (
        "Hammer|Tools|10\n"
        "Screwdriver|Tools|4\n"
        "Apple|Food|5\n"
        "Bread|Food|2\n"
    )

    # Act
    save_inventory(sample_inventory, file_path)
    contents = file_path.read_text(encoding="utf-8")

    # Assert
    assert contents == expected


def test_save_empty_inventory(tmp_path, empty_inventory):
    # Arrange
    file_path = tmp_path / "inventory.txt"

    # Act
    save_inventory(empty_inventory, file_path)
    contents = file_path.read_text(encoding="utf-8")

    # Assert
    assert contents == ""


def test_save_load_round_trip(tmp_path, sample_inventory):
    # Arrange
    file_path = tmp_path / "inventory.txt"

    # Act
    save_inventory(sample_inventory, file_path)
    loaded_inventory = load_inventory(file_path)

    # Assert
    assert loaded_inventory == sample_inventory

# --------------------------------------------------
# Search Tests
# --------------------------------------------------

def test_search_exact_name(sample_inventory):
    # Arrange
    search_term = "Hammer"

    # Act
    matches = find_matching_items(sample_inventory, search_term)

    # Assert
    assert matches == [sample_inventory[0]]


def test_search_partial_name(sample_inventory):
    # Arrange
    search_term = "Ham"

    # Act
    matches = find_matching_items(sample_inventory, search_term)

    # Assert
    assert matches == [sample_inventory[0]]


def test_search_ignores_capitalization(sample_inventory):
    # Arrange
    search_term = "HAMMER"

    # Act
    matches = find_matching_items(sample_inventory, search_term)

    # Assert
    assert matches == [sample_inventory[0]]


def test_search_multiple_matches():
    # Arrange
    inventory = [
        {"name": "Red Apple", "category": "Food", "quantity": 5},
        {"name": "Green Apple", "category": "Food", "quantity": 3},
        {"name": "Hammer", "category": "Tools", "quantity": 10}
    ]

    # Act
    matches = find_matching_items(inventory, "Apple")

    # Assert
    assert len(matches) == 2
    assert matches[0]["name"] == "Red Apple"
    assert matches[1]["name"] == "Green Apple"


def test_search_no_matches(sample_inventory):
    # Arrange
    search_term = "Computer"

    # Act
    matches = find_matching_items(sample_inventory, search_term)

    # Assert
    assert matches == []


@pytest.mark.parametrize(
    "search_term",
    ["", " ", "   "],
    ids=["empty", "one-space", "multiple-spaces"]
)
def test_search_empty_or_whitespace(sample_inventory, search_term):
    # Arrange
    expected = []

    # Act
    matches = find_matching_items(sample_inventory, search_term)

    # Assert
    assert matches == expected


# --------------------------------------------------
# Remove-Item Tests
# --------------------------------------------------

@pytest.mark.parametrize(
    "item_number, expected_removed, expected_remaining",
    [
        (1, "Hammer", ["Screwdriver", "Apple", "Bread"]),
        (2, "Screwdriver", ["Hammer", "Apple", "Bread"]),
        (4, "Bread", ["Hammer", "Screwdriver", "Apple"])
    ],
    ids=["remove-first", "remove-middle", "remove-last"]
)
def test_remove_item_positions(
    sample_inventory,
    item_number,
    expected_removed,
    expected_remaining
):
    # Arrange
    inventory = sample_inventory

    # Act
    removed = remove_item_by_number(inventory, item_number)

    remaining_names = [item["name"] for item in inventory]

    # Assert
    assert removed["name"] == expected_removed
    assert remaining_names == expected_remaining


@pytest.mark.parametrize(
    "item_number",
    [0, -1, 5, 100],
    ids=["zero", "negative", "one-past-end", "far-out-of-range"]
)
def test_remove_invalid_item_number(sample_inventory, item_number):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    removed = remove_item_by_number(sample_inventory, item_number)

    # Assert
    assert removed is None
    assert sample_inventory == original_inventory

# --------------------------------------------------
# Update-Quantity Tests
# --------------------------------------------------

def test_update_valid_quantity(sample_inventory):
    # Arrange
    item_number = 1
    new_quantity = 20

    # Act
    result = update_item_quantity(
        sample_inventory, item_number, new_quantity
    )

    # Assert
    assert result is True
    assert sample_inventory[0]["quantity"] == 20


def test_update_quantity_to_zero(sample_inventory):
    # Arrange
    item_number = 1
    new_quantity = 0

    # Act
    result = update_item_quantity(
        sample_inventory, item_number, new_quantity
    )

    # Assert
    assert result is True
    assert sample_inventory[0]["quantity"] == 0


def test_update_correct_item_only(sample_inventory):
    # Arrange
    original_other_items = [
        item.copy() for item in sample_inventory[1:]
    ]

    # Act
    result = update_item_quantity(sample_inventory, 2, 15)

    # Assert
    assert result is True
    assert sample_inventory[1]["quantity"] == 15
    assert sample_inventory[0]["quantity"] == 10
    assert sample_inventory[2:] == original_other_items


@pytest.mark.parametrize(
    "item_number",
    [0, -1, 5, 100],
    ids=["zero", "negative", "one-past-end", "far-out-of-range"]
)
def test_update_invalid_item_number(sample_inventory, item_number):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = update_item_quantity(sample_inventory, item_number, 10)

    # Assert
    assert result is False
    assert sample_inventory == original_inventory


def test_update_negative_quantity(sample_inventory):
    # Arrange
    original_inventory = [item.copy() for item in sample_inventory]

    # Act
    result = update_item_quantity(sample_inventory, 1, -5)

    # Assert
    assert result is False
    assert sample_inventory == original_inventory


# --------------------------------------------------
# Add-Item Validation Tests
# --------------------------------------------------

def test_validate_normal_item(sample_inventory):
    # Arrange
    name = "Wrench"
    category = "Tools"
    quantity = 8

    # Act
    result = validate_new_item(
        sample_inventory, name, category, quantity
    )

    # Assert
    assert result is True


@pytest.mark.parametrize(
    "name, category, quantity",
    [
        ("", "Tools", 5),
        ("   ", "Tools", 5),
        ("Hammer", "", 5),
        ("Hammer", "   ", 5),
        ("Bad|Name", "Tools", 5),
        ("Wrench", "Bad|Category", 5),
        ("Wrench", "Tools", -1),
        ("Hammer", "Tools", 5),
        ("hAmMeR", "Tools", 5)
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
        "duplicate-different-capitalization"
    ]
)
def test_validate_invalid_item(
    sample_inventory, name, category, quantity
):
    # Arrange
    inventory = sample_inventory

    # Act
    result = validate_new_item(inventory, name, category, quantity)

    # Assert
    assert result is False


@pytest.mark.parametrize(
    "quantity",
    ["five", "5", 5.5, True],
    ids=["text", "numeric-string", "decimal", "boolean"]
)
def test_validate_invalid_quantity(sample_inventory, quantity):
    # Arrange
    name = "Wrench"
    category = "Tools"

    # Act
    result = validate_new_item(
        sample_inventory, name, category, quantity
    )

    # Assert
    assert result is False
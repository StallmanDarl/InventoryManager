import pytest

from inventory_manager import (
    load_inventory,
    save_inventory
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
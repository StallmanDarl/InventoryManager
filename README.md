# Inventory Manager

## Project Description

Inventory Manager is a command-line Python application that helps users manage inventory for a small organization. Users can view, add, update, remove, and search inventory items. The application also provides a summary of inventory quantities and categories.

Inventory records are stored in a text file named `inventory.txt`, allowing saved changes to remain available after the program closes.

This project demonstrates Python functions, lists, dictionaries, loops, conditionals, input validation, file handling, testing, and Git/GitHub version control.

## Features

- **View inventory:** Display all items in a numbered list.
- **Add items:** Add new items with a name, category, and quantity.
- **Update quantities:** Change the quantity of an existing item.
- **Remove items:** Delete an item from the inventory.
- **Search inventory:** Search item names using partial matches without regard to capitalization.
- **Inventory summary:** Display the number of items, total quantity, low-stock count, and category counts.
- **Input validation:** Reject invalid quantities, duplicate names, invalid item selections, and other invalid inputs.
- **File persistence:** Load inventory when the program starts and save changes to `inventory.txt`.
- **Missing-file handling:** Start with an empty inventory if the inventory file does not exist.

An item is considered low stock when its quantity is below 5.

## Requirements

- Python 3
- A terminal or command-line interface
- Git for version control
- A GitHub account to access or contribute to the repository

No external Python packages are required.

## Project Files

| File | Description |
|---|---|
| `inventory_manager.py` | Main Python application and required functions |
| `inventory.txt` | Text file containing inventory records |
| `README.md` | Project description and usage instructions |
| `TESTING.md` | Inventory Manager testing plan and results |
| `AI_USAGE.md` | Disclosure of AI tools and assistance |
| `.gitignore` | Excludes unnecessary files and sensitive local configuration |

## Inventory Data Format

Inventory data is stored in `inventory.txt`, with one item per line. Each line contains three fields separated by the pipe character (`|`):

```text
Name|Category|Quantity
```

Example:

```text
Laptop Charger|Electronics|8
Printer Paper|Office Supplies|25
Dry-Erase Markers|Classroom Supplies|4
USB-C Cable|Electronics|12
Notebook|Classroom Supplies|3
Safety Goggles|Workshop Tools|10
```

The fields represent:

1. **Name:** The inventory item's name.
2. **Category:** The item's category.
3. **Quantity:** The current quantity, stored as a nonnegative whole number.

Item names and categories cannot contain the pipe character because it separates the fields.

Item names must be unique regardless of capitalization. For example, `Laptop Charger` and `laptop charger` are considered duplicates.

## Installation and Setup

### 1. Clone the repository

Open PowerShell or another terminal and run:

```powershell
git clone https://github.com/YOUR-USERNAME/InventoryManager.git
```

Replace `YOUR-USERNAME` with the GitHub username that owns the repository.

### 2. Enter the project directory

```powershell
cd InventoryManager
```

### 3. Verify Python

```powershell
python --version
```

If `python` is not recognized on Windows, try:

```powershell
py --version
```

### 4. Run the application

Using Python:

```powershell
python inventory_manager.py
```

Alternatively, on Windows:

```powershell
py inventory_manager.py
```

The program loads the existing inventory file when it starts. If `inventory.txt` does not exist, it begins with an empty inventory.

Run the application from the project directory so it uses the intended `inventory.txt` file.

## Menu Options

When the program starts, it displays the following menu:

```text
Inventory Manager

1. View inventory
2. Add an item
3. Update an item quantity
4. Remove an item
5. Search inventory
6. View inventory summary
7. Exit
```

| Option | Description |
|---|---|
| 1 | Display all inventory items |
| 2 | Add a new item after validating its information |
| 3 | Update the quantity of a selected item |
| 4 | Remove a selected item |
| 5 | Search item names using partial, case-insensitive matching |
| 6 | Display inventory totals and category counts |
| 7 | Exit the application |

Invalid menu choices display an error message, and the menu appears again.

### Viewing Inventory

The program displays each item with a number, name, category, and quantity.

Example:

```text
Inventory:
1. Laptop Charger | Electronics | Quantity: 8
2. Printer Paper | Office Supplies | Quantity: 25
3. Dry-Erase Markers | Classroom Supplies | Quantity: 4
```

If the inventory is empty, the program displays:

```text
No inventory items found.
```

### Adding an Item

Select option 2 and enter the requested information.

Example:

```text
Enter the item name: HDMI Cable
Enter the category: Electronics
Enter the quantity: 6
Item added successfully.
```

The program rejects empty names, empty categories, duplicate names, names or categories containing `|`, nonnumeric quantities, and negative quantities.

Successfully added items are saved to `inventory.txt`.

### Updating an Item

Select option 3, choose an item by its displayed number, and enter the new quantity.

Example:

```text
Enter the item number to update: 1
Enter the new quantity: 12
Laptop Charger quantity updated to 12.
```

The program validates the selection and quantity before updating the record.

### Removing an Item

Select option 4 and enter the number of the item to remove.

Example:

```text
Enter the item number to remove: 2
Item removed: Printer Paper
```

The removed item is deleted from the inventory and the updated list is saved.

### Searching Inventory

Select option 5 and enter all or part of an item name.

Searches ignore capitalization and can return multiple matching items.

For example, searching for `charger` can match both `Laptop Charger` and `USB-C Charger`.

If there are no matches, the program displays:

```text
No inventory items matched your search.
```

Empty or whitespace-only searches are rejected.

### Viewing the Inventory Summary

Select option 6 to display inventory statistics.

The summary includes:

- Number of unique inventory items
- Total quantity across all inventory records
- Number of low-stock items with quantities below 5
- Number of items in each category

Category counts ignore capitalization differences. For example, `Electronics` and `electronics` count as the same category.

### Exiting the Application

Select option 7 to display a goodbye message and end the program.

All successful additions, quantity updates, and removals are saved before the application exits.

## Testing

Testing procedures and results are documented in [`TESTING.md`](TESTING.md).

The testing plan covers:

- Loading a missing inventory file
- Viewing an empty inventory
- Adding valid and invalid items
- Rejecting duplicate names
- Validating quantities and item selections
- Updating and removing items
- Case-insensitive partial searching
- Handling searches with no matches
- Verifying inventory summaries
- Confirming persistence after restarting

**Testing status:** Consult `TESTING.md` for the actual results. Only tests that have been executed should be marked as passing.

## Git and GitHub Development

Git is used to track incremental development, while GitHub hosts the remote repository and documents the search feature workflow.

The development process includes:

1. Creating and initializing the local repository.
2. Committing the initial project structure and `.gitignore`.
3. Implementing inventory file handling and item management.
4. Creating a GitHub issue for case-insensitive inventory search.
5. Developing search on the `feature/inventory-search` branch.
6. Pushing the feature branch to GitHub.
7. Opening and reviewing a pull request into `main`.
8. Merging the pull request using **Create a merge commit**.
9. Completing the summary, testing, and documentation.
10. Synchronizing the local and remote `main` branches.

The repository's Git history provides the actual record of development commits. The merged pull request and related issue provide evidence of the feature development workflow.

## AI Usage

AI assistance, if used, is documented in [`AI_USAGE.md`](AI_USAGE.md).

The report describes the tools used, example prompts, accepted and modified suggestions, verification procedures, and understanding of AI-assisted work.

All submitted code and documentation must be reviewed and understood by the student.

## Known Limitations

- Inventory data is stored in a local text file rather than a database.
- The program is designed for one user at a time.
- Item names and categories cannot contain the pipe separator.
- Inventory records are expected to follow the specified three-field format.
- The program does not provide user accounts or access permissions.
- Inventory changes must be made through the command-line interface or by editing the data file manually.

## Possible Future Improvements

- Sort items by name, category, or quantity.
- Filter inventory by category.
- Warn users when quantities fall below a configurable threshold.
- Export inventory summaries to CSV.
- Add automated unit tests.
- Introduce a graphical user interface.
- Use a database for larger inventories.
- Add item identifiers, suppliers, prices, and restocking information.

## License

No license has been specified for this project. Unless a license is added, users should not assume that the repository grants permission to reuse or redistribute its code.

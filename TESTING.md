# Inventory Manager Testing

## Testing Overview

This document records tests for the Inventory Manager command-line Python application.

Testing covers inventory loading and saving, item management, input validation, searching, summary calculations, and persistence between program runs.

## Test Environment

| Environment Detail | Value |
|---|---|
| Operating system | Windows 11, 64-bit |
| Programming language | Python 3 |
| Application | `inventory_manager.py` |
| Inventory data file | `inventory.txt` |
| Testing method | Manual command-line testing |
| Development environment | Visual Studio Code |
| Python version | Python 3.x; exact version not recorded |

## Test Cases

| # | Feature | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Missing inventory file | Rename `inventory.txt` and start the program | Program starts and uses an empty inventory | Program started without crashing and handled the missing file | Pass |
| 2 | View empty inventory | Select option 1 with no items | Displays `No inventory items found.` | Empty-inventory message displayed | Pass |
| 3 | Add valid item | Enter a valid name, category, and quantity | Item is added and saved | Item was added successfully and saved in the expected format | Pass |
| 4 | Reject empty name | Submit an empty item name | Error displayed; item not added | Empty name was rejected | Pass |
| 5 | Reject duplicate name | Add an existing name with different capitalization | Duplicate-name error displayed | Duplicate name was rejected without adding another record | Pass |
| 6 | Reject nonnumeric quantity | Enter `six` as the quantity | Quantity error displayed | Invalid quantity was rejected | Pass |
| 7 | Reject negative quantity | Enter `-3` as the quantity | Quantity error displayed | Negative quantity was rejected | Pass |
| 8 | Update valid item | Select an item and enter a valid quantity | Item updated and change saved | Selected item's quantity was updated and saved | Pass |
| 9 | Reject invalid item number | Enter text or an out-of-range number | Invalid selection rejected | Invalid item selections were rejected without changing inventory | Pass |
| 10 | Remove item | Select an existing item | Item removed and change saved | Selected item was removed from the inventory and saved file | Pass |
| 11 | Case-insensitive partial search | Search for `CHARGER` or `laptop` | All matching items displayed | Partial matches were found regardless of capitalization | Pass |
| 12 | Search with no matches | Search for `xyz123` | No-match message displayed | `No inventory items matched your search.` displayed | Pass |
| 13 | Inventory summary | Use a known inventory dataset | Correct counts and totals displayed | Item count, quantity total, low-stock count, and category counts matched the expected values | Pass |
| 14 | Persistence after restart | Add an item, exit, restart, and view inventory | Item remains saved | Added item remained available after restarting the program | Pass |
| 15 | Reject empty category | Submit an empty category | Error displayed; item not added | Empty category was rejected | Pass |
| 16 | Reject separator character | Enter `\|` in a name or category | Invalid input rejected | Separator input was rejected to protect the file format | Pass |
| 17 | Invalid menu choice | Enter `hello` or `8` | Error displayed and menu returns | Invalid menu selections were handled without crashing | Pass |
| 18 | Empty-inventory update and removal | Select update and remove with no items | Operations handled safely | Both operations handled the empty inventory without crashing | Pass |
| 19 | Invalid update quantity | Enter text or a negative quantity | Error displayed; original quantity retained | Invalid quantities were rejected and the original quantity remained unchanged | Pass |
| 20 | Whitespace-only search | Search using only spaces | Empty-search error displayed | Blank search was rejected | Pass |
| 21 | Category capitalization | Use categories differing only in capitalization | Categories counted together | Capitalization variants were treated as the same category | Pass |
| 22 | Zero quantity | Add an item with quantity `0` | Item accepted and counted as low stock | Zero quantity was accepted and the item was counted as low stock | Pass |

## Detailed Testing Procedures

### Test 1: Missing Inventory File

1. Close the application.
2. Back up `inventory.txt`.
3. Temporarily rename or move the file.
4. Start `inventory_manager.py`.
5. Select option 1.
6. Confirm the program starts and handles the empty inventory.
7. Restore the original file.

**Pass condition:** The program handles a missing file without crashing.

**Result:** Pass.

### Test 2: Empty Inventory

1. Use an empty inventory file or temporarily move the existing file.
2. Start the program.
3. Select option 1.
4. Confirm the empty-inventory message appears.
5. Select options 3 and 4 to test updating and removing items.
6. Restore the original inventory.

**Pass condition:** Empty-inventory operations do not cause a crash.

**Result:** Pass.

### Test 3: Add a Valid Item

1. Start the application.
2. Select option 2.
3. Enter a new item name, a category, and a nonnegative whole-number quantity.
4. Confirm the success message.
5. Open `inventory.txt`.
6. Verify the item appears as `Name|Category|Quantity`.

**Pass condition:** The item is added and saved in the required format.

**Result:** Pass.

### Test 4: Reject an Empty Name

1. Select option 2.
2. Submit an empty name.
3. Observe the error message.
4. Confirm no item was added.

**Pass condition:** Empty names are rejected without changing inventory data.

**Result:** Pass.

### Test 5: Reject a Duplicate Name

1. Confirm `Laptop Charger` exists.
2. Select option 2.
3. Enter `laptop charger` as the new name.
4. Observe the duplicate-name error.
5. Confirm no duplicate record was added.

**Pass condition:** Names differing only in capitalization are treated as duplicates.

**Result:** Pass.

### Test 6: Reject a Nonnumeric Quantity

1. Select option 2.
2. Enter a valid name and category.
3. Enter `six` as the quantity.
4. Observe the error message.
5. Confirm the item was not added.

**Pass condition:** Invalid numeric input is rejected.

**Result:** Pass.

### Test 7: Reject a Negative Quantity

1. Select option 2.
2. Enter a valid name and category.
3. Enter `-3` as the quantity.
4. Observe the error message.
5. Confirm the item was not added.

**Pass condition:** Negative quantities are rejected.

**Result:** Pass.

### Test 8: Update an Item

1. Confirm an item exists.
2. Select option 3.
3. Choose its displayed number.
4. Enter a new nonnegative quantity.
5. Confirm the success message.
6. Check `inventory.txt` for the updated quantity.

**Pass condition:** The correct item is updated and the change is saved.

**Result:** Pass.

### Test 9: Reject an Invalid Item Number

1. Select option 3.
2. Enter a nonnumeric selection such as `abc`.
3. Repeat with a number outside the available range.
4. Observe the error messages.
5. Confirm the inventory remains unchanged.

**Pass condition:** Invalid selections are rejected without crashing or changing inventory data.

**Result:** Pass.

### Test 10: Remove an Item

1. Confirm the inventory contains an item.
2. Select option 4.
3. Choose the item by its displayed number.
4. Confirm the removal message.
5. Inspect the inventory and `inventory.txt`.

**Pass condition:** The selected item is removed from memory and the saved file.

**Result:** Pass.

### Test 11: Case-Insensitive Partial Search

1. Ensure `Laptop Charger` and `USB-C Cable` exist.
2. Select option 5.
3. Search for `CHARGER`.
4. Repeat with `laptop`.
5. Confirm all matching items appear.

**Pass condition:** Partial searches find matching names regardless of capitalization.

**Result:** Pass.

### Test 12: Search With No Matches

1. Select option 5.
2. Enter `xyz123`.
3. Observe the output.

**Pass condition:** The program displays `No inventory items matched your search.`

**Result:** Pass.

### Test 13: Verify Inventory Summary

1. Prepare a known dataset.
2. Count the item records.
3. Add the quantities.
4. Count items with quantities below five.
5. Count each category while ignoring capitalization.
6. Select option 6.
7. Compare the displayed results with the calculated values.

**Pass condition:** All counts and totals match the expected results.

**Result:** Pass.

### Test 14: Persistence After Restart

1. Start the application.
2. Add an item with a unique name and valid quantity.
3. Exit using option 7.
4. Confirm the item appears in `inventory.txt`.
5. Restart the application.
6. Select option 1.
7. Confirm the item and quantity remain available.

**Pass condition:** Saved changes persist after restarting.

**Result:** Pass.

## Additional Tests

### Test 15: Reject an Empty Category

**Procedure:** Attempt to add an item with a valid name but an empty category.

**Expected result:** The category is rejected, and no item is added.

**Result:** Pass.

### Test 16: Reject the File Separator

**Procedure:** Attempt to include `|` in an item name or category.

**Expected result:** The input is rejected to prevent malformed inventory records.

**Result:** Pass.

### Test 17: Invalid Menu Choice

**Procedure:** Enter `hello` and an out-of-range menu option such as `8`.

**Expected result:** The program reports an invalid choice and returns to the menu.

**Result:** Pass.

### Test 18: Update and Remove With Empty Inventory

**Procedure:** Attempt to update and remove items while the inventory is empty.

**Expected result:** The program handles both operations safely without crashing.

**Result:** Pass.

### Test 19: Invalid Update Quantity

**Procedure:** Select an existing item and attempt to update its quantity using text or a negative number.

**Expected result:** The invalid quantity is rejected, and the original quantity remains unchanged.

**Result:** Pass.

### Test 20: Whitespace-Only Search

**Procedure:** Select option 5 and enter only spaces.

**Expected result:** The search is rejected as empty.

**Result:** Pass.

### Test 21: Category Capitalization

**Procedure:** Prepare records whose category names differ only in capitalization and view the summary.

**Expected result:** Capitalization variants are counted as one category.

**Result:** Pass.

### Test 22: Zero Quantity

**Procedure:** Add an item with a quantity of `0`.

**Expected result:** The item is accepted and counted as low stock.

**Result:** Pass.

## Testing Summary

| Result | Count |
|---|---:|
| Total tests | 22 |
| Tests passed | 22 |
| Tests failed | 0 |
| Outstanding tests | 0 |

**Issues found and corrected:** No unresolved issues were recorded in this test summary.

## Final Testing Assessment

The Inventory Manager was evaluated against its required functionality, including loading and saving inventory, adding and updating items, removing items, searching, input validation, summary calculations, and persistence between program runs.

The recorded results indicate that all 22 test cases passed and that the application met the tested requirements. The testing results apply to the tested environment and dataset; additional testing may be needed if the program or its requirements change.
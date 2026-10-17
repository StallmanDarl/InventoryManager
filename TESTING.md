# Inventory Manager Testing

## Testing Overview

This document records tests for the Inventory Manager command-line Python application.

Testing verifies inventory loading and saving, item management, input validation, searching, summary calculations, and persistence between program runs.

Tests should be performed using the actual application. The expected results describe the required behavior; the actual results and pass/fail status must reflect the observed outcome.

## Test Environment

Complete this section with your actual environment.

| Environment Detail | Value |
|---|---|
| Operating system | Windows |
| Programming language | Python 3 |
| Application | `inventory_manager.py` |
| Inventory data file | `inventory.txt` |
| Testing method | Manual command-line testing |
| Python version | Record the output of `python --version` |

## Test Cases

| # | Feature | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Missing inventory file | Temporarily move or rename `inventory.txt`, then start the program | Program starts without crashing and uses an empty inventory | Not yet tested | Pending |
| 2 | View empty inventory | Start with an empty inventory and select option 1 | Displays `No inventory items found.` | Not yet tested | Pending |
| 3 | Add valid item | Enter a new name, category, and nonnegative whole-number quantity | Item is added successfully and saved to `inventory.txt` | Not yet tested | Pending |
| 4 | Reject empty name | Select option 2 and submit an empty item name | Displays an error and does not add an item | Not yet tested | Pending |
| 5 | Reject duplicate name | Add an existing name using different capitalization | Displays a duplicate-name error and does not add another record | Not yet tested | Pending |
| 6 | Reject nonnumeric quantity | Enter `six` as the quantity when adding an item | Displays `Quantity must be a nonnegative whole number.` and does not add the item | Not yet tested | Pending |
| 7 | Reject negative quantity | Enter `-3` as the quantity when adding an item | Displays a quantity error and does not add the item | Not yet tested | Pending |
| 8 | Update valid item | Select an existing item and enter a valid new quantity | Displays the item name and new quantity; saves the change | Not yet tested | Pending |
| 9 | Reject invalid item number | Enter a nonnumeric selection or a number outside the available range when updating an item | Displays `Invalid item number.` and leaves the inventory unchanged | Not yet tested | Pending |
| 10 | Remove item | Select an existing item by its displayed number | Displays the removed item's name and saves the updated inventory | Not yet tested | Pending |
| 11 | Case-insensitive partial search | Search for part of an item name using different capitalization | Displays every item whose name contains the search term | Not yet tested | Pending |
| 12 | Search with no matches | Search for a term that does not occur in any item name | Displays `No inventory items matched your search.` | Not yet tested | Pending |
| 13 | Inventory summary | View the summary using a known inventory dataset | Displays correct unique-item count, total quantity, low-stock count, and category counts | Not yet tested | Pending |
| 14 | Persistence after restart | Add an item, exit, restart the application, and view the inventory | The added item and its quantity remain saved | Not yet tested | Pending |
| 15 | Reject empty category | Enter a valid item name and then submit an empty category | Displays an error and does not add an item | Not yet tested | Pending |
| 16 | Reject separator character | Enter `|` in an item name or category | Rejects the input and does not create a malformed record | Not yet tested | Pending |
| 17 | Invalid menu choice | Enter an invalid option such as `hello` or `8` | Displays a menu error and returns to the menu | Not yet tested | Pending |
| 18 | Empty-inventory update and removal | Select options 3 and 4 while the inventory is empty | Handles both operations safely without crashing | Not yet tested | Pending |
| 19 | Invalid update quantity | Select a valid item and enter text or a negative quantity | Displays a quantity error and leaves the original quantity unchanged | Not yet tested | Pending |
| 20 | Whitespace-only search | Select option 5 and enter only spaces | Displays an empty-search error and returns to the menu | Not yet tested | Pending |
| 21 | Category capitalization | Use records whose categories differ only in capitalization and view the summary | Treats capitalization variants as the same category | Not yet tested | Pending |
| 22 | Zero quantity | Add an item with quantity `0` | Accepts the item and counts it as low stock | Not yet tested | Pending |

## Detailed Testing Procedures

### Test 1: Missing Inventory File

1. Close the application.
2. Make a backup of `inventory.txt` outside the project folder.
3. Temporarily rename or move `inventory.txt`.
4. Start `inventory_manager.py`.
5. Select option 1.
6. Confirm that the application starts and displays the empty-inventory message.
7. Restore the original file.

**Pass condition:** The program handles the missing file without crashing.

### Test 2: Empty Inventory

1. Temporarily use an empty inventory file or repeat the missing-file setup.
2. Start the program.
3. Select option 1.
4. Confirm that the empty-inventory message appears.
5. Select options 3 and 4 to verify that updating and removing items are handled safely.
6. Restore the original inventory.

**Pass condition:** Empty inventory operations do not cause an error or crash.

### Test 3: Add a Valid Item

1. Start the application.
2. Select option 2.
3. Enter a new item name, a nonempty category, and a valid nonnegative quantity.
4. Confirm the success message.
5. Open `inventory.txt`.
6. Verify that the item appears as `Name|Category|Quantity`.

**Pass condition:** The item is added to memory and saved in the required format.

### Test 4: Reject an Empty Name

1. Select option 2.
2. Submit an empty name.
3. Observe the error message.
4. View the inventory and confirm that no item was added.

**Pass condition:** The empty name is rejected without changing inventory data.

### Test 5: Reject a Duplicate Name

1. Confirm that an item named `Laptop Charger` exists.
2. Select option 2.
3. Enter `laptop charger` as the new name.
4. Observe the duplicate-name error.
5. Check that the inventory still contains only one record with that name.

**Pass condition:** Names that differ only in capitalization are treated as duplicates.

### Test 6: Reject a Nonnumeric Quantity

1. Select option 2.
2. Enter a valid new name and category.
3. Enter `six` as the quantity.
4. Observe the quantity error.
5. Confirm that the item was not added.

**Pass condition:** The program rejects text that cannot represent a valid quantity.

### Test 7: Reject a Negative Quantity

1. Select option 2.
2. Enter a valid name and category.
3. Enter `-3` as the quantity.
4. Observe the error message.
5. Confirm that the item was not added.

**Pass condition:** Negative quantities are rejected.

### Test 8: Update an Item

1. Confirm that an item exists in the inventory.
2. Select option 3.
3. Choose its displayed number.
4. Enter a new nonnegative quantity.
5. Confirm the success message.
6. Check `inventory.txt` for the updated quantity.

**Pass condition:** The correct item is updated and the change persists in the file.

### Test 9: Reject an Invalid Item Number

1. Select option 3.
2. Enter a nonnumeric selection, such as `abc`.
3. Repeat and enter a number larger than the number of available items.
4. Observe the error messages.
5. Confirm that no item was changed.

**Pass condition:** Invalid selections are rejected without crashing or modifying the inventory.

### Test 10: Remove an Item

1. Confirm that the inventory contains at least one item.
2. Select option 4.
3. Choose an existing item by its displayed number.
4. Confirm the removal message.
5. View the inventory and inspect `inventory.txt`.

**Pass condition:** The selected item is removed from both the in-memory inventory and saved file.

### Test 11: Case-Insensitive Partial Search

1. Ensure that the inventory contains `Laptop Charger` and `USB-C Cable`.
2. Select option 5.
3. Search for `CHARGER`.
4. Repeat with `laptop`.
5. If two or more names contain the search term, confirm that every matching item appears.

**Pass condition:** Partial matches are found regardless of capitalization.

### Test 12: Search With No Matches

1. Select option 5.
2. Enter a search term that does not occur in any item name, such as `xyz123`.
3. Observe the output.

**Pass condition:** The program displays `No inventory items matched your search.`

### Test 13: Verify Inventory Summary

1. Prepare a known dataset.
2. Calculate the number of item records.
3. Add all quantities to calculate the total.
4. Count the items with quantities below 5.
5. Count the items in each category, ignoring capitalization differences.
6. Select option 6.
7. Compare the displayed results with your calculations.

**Pass condition:** All displayed counts and totals match the expected values.

### Test 14: Persistence After Restart

1. Start the application.
2. Add an item with a unique name and a valid quantity.
3. Exit using option 7.
4. Confirm that the item is present in `inventory.txt`.
5. Start the application again.
6. Select option 1.
7. Confirm that the item is still present with the correct quantity.

**Pass condition:** Saved changes remain available after restarting the program.

## Recording Results

After running each test:

1. Replace `Not yet tested` with a concise description of the observed behavior.
2. Change `Pending` to `Pass` or `Fail` based on the actual result.
3. If a test fails, record what happened.
4. Fix the problem in the program.
5. Repeat the test.
6. Record the final result accurately.

Do not mark a test as passed based only on reading the code.

## Testing Summary

Complete this section after testing.

- **Total tests executed:** [Enter the actual number]
- **Tests passed:** [Enter the actual number]
- **Tests failed:** [Enter the actual number]
- **Outstanding tests:** [Enter the actual number]
- **Issues found and corrected:** [Describe actual issues or write "None observed" if appropriate]

The final submission must include at least 14 completed tests. Additional tests are included in this document to cover more edge cases.

## Final Testing Assessment

[Summarize whether the application met the requirements based on the completed tests. Mention any remaining defects or limitations.]


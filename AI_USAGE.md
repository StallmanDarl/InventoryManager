# AI Usage Report

## Tools Used

- **ChatGPT (OpenAI):** Used occasionally for programming guidance, debugging assistance, documentation suggestions, and help organizing automated tests.
- **Visual Studio Code:** Used to write, edit, test, and manage the project files. This is a development tool, not an AI tool.
- **pytest:** Used to run automated tests and verify the Inventory Manager's functionality.

## How AI Was Used

I completed most of the Inventory Manager project myself, including implementing the main program, managing inventory data, debugging problems, refactoring functions, writing tests, and managing project files.

ChatGPT was used as a supplementary resource for explaining programming concepts, suggesting improvements, organizing documentation, and providing ideas for additional test cases. It also helped me understand pytest features, improve test organization, and review the project's README and testing documentation.

I was responsible for implementing, reviewing, modifying, and verifying the final code. AI assistance did not replace my own work or responsibility for meeting the assignment requirements.

## Example Prompts

The following are representative prompts used to request assistance:

1. "Explain how I should organize the README.md file."
2. "Create a TESTING.md file with test cases for loading, saving, searching, updating, and removing inventory items."
3. "Update README.md according to the new commits."
4. "Based on this, provide the updated test."
5. "This test fails. Explain why and how to correct it."

These prompts primarily requested documentation assistance, testing suggestions, debugging explanations, and help organizing the project.

## Suggestions Accepted

Some useful suggestions from ChatGPT included:

- Organizing the README into sections covering project features, installation, usage, file format, and testing.
- Separating important inventory operations into independent functions to make them easier to test.
- Creating test cases for loading, saving, searching, adding, updating, removing, and calculating inventory summaries.
- Using pytest fixtures to provide reusable sample inventory data.
- Using parameterized tests to check multiple inputs and expected results.
- Using `tmp_path` to test file operations without modifying the actual inventory file.
- Adding descriptive test IDs and Arrange-Act-Assert sections to improve test readability.
- Using clear Git commit messages and feature branches to organize development.

I reviewed these suggestions and adapted the useful ones to fit my implementation and assignment requirements.

## Suggestions Rejected or Modified

Some suggestions and examples required modification before they could be used.

For example, an initial search test expected three matching items when searching for the letter `e`. However, all four sample inventory item names contained that letter. I corrected the expected result to four after reviewing the test output.

Generic testing instructions and sample results were also not treated as proof that the program worked. Tests needed to be executed, and actual results needed to be recorded rather than assumed.

I also adapted documentation and code examples to match the actual filenames, program behavior, repository structure, and assignment requirements.

## Verification

I was responsible for verifying the final project. AI-generated suggestions were not treated as proof that the program worked.

Verification included reviewing and testing the following functionality:

- Loading inventory from a data file and handling missing files.
- Saving multiple inventory items using the required `Name|Category|Quantity` format.
- Saving an empty inventory and testing save/load round trips.
- Displaying inventory items and summary information.
- Adding, updating, and removing inventory items.
- Rejecting invalid input, including negative quantities, empty fields, and duplicate names.
- Searching using exact, partial, and case-insensitive matching.
- Handling empty searches and searches with no matches.
- Checking low-stock counts and category totals.
- Reviewing the README, testing documentation, and AI usage report for accuracy.

The automated test suite uses pytest to verify these operations. The final regression results should be recorded in `TESTING.md` after running the complete test suite.

## Code Understanding

AI assistance focused primarily on explanations, documentation, debugging guidance, and testing suggestions. I remained responsible for understanding and maintaining the program's implementation.

Two important parts of the project are:

**1. Inventory Search**

The search feature compares the user's search text with inventory item names without requiring an exact match. Case-insensitive matching allows searches such as `cable` to find an item named `USB-C Cable`. Partial matching makes searching more flexible because users do not need to enter the complete item name. The program also handles blank searches and returns an empty result when no items match.

**2. Inventory Summary**

The summary feature calculates information from the current inventory list. It counts inventory entries, adds their quantities to determine the total quantity, identifies items with quantities below five, and groups items by category. Category comparisons ignore capitalization so that variations in capitalization do not incorrectly create separate categories.

Understanding these operations allows me to explain the program's behavior, evaluate whether its results are correct, and maintain the code independently.
# AI Usage Report

## Tools Used

- **ChatGPT (OpenAI):** Used for occasional programming guidance, documentation assistance, and suggestions for testing and organizing the project.
- **Visual Studio Code:** Used to write, edit, and manage the project files. This is a development tool, not an AI tool.

## How AI Was Used

I completed most of the Inventory Manager project myself, including implementing the main program, working with the inventory data, debugging problems, and managing the project files.

ChatGPT was used as a supplementary tool for simple tasks, such as explaining programming concepts, suggesting improvements to documentation, organizing the README and testing documentation, and providing ideas for additional test cases. It also helped me understand how to document the project's features, setup instructions, and Git workflow.

AI assistance was not a substitute for my own work. I was responsible for implementing, reviewing, modifying, and verifying the project. I also needed to ensure that the final program followed the assignment requirements.

## Example Prompts

The following are representative prompts used to request assistance with the project:

1. "Explain how I should organize the README.md file."
2. "Create a TESTING.md file with test cases for loading, saving, searching, updating, and removing inventory items."
3. "Update README.md according to the new commits."

These prompts primarily requested help with documentation, testing organization, and updating .md files.

## Suggestions Accepted

Some useful suggestions from ChatGPT included:

- Organizing the README into sections covering project features, installation, usage, file format, and testing.
- Creating a testing checklist that covers normal operations, invalid input, missing files, and inventory search behavior.
- Documenting the expected behavior of inventory quantities, category summaries, and low-stock items.
- Using clear Git commit messages and a feature branch when implementing the inventory search functionality.
- Reviewing the final documentation to make it easier for another person to understand and run the project.

I considered these suggestions in relation to the assignment requirements and used or adapted the ones that were useful.

## Suggestions Rejected or Modified

Some suggestions and documentation examples required modification before they could be used.

For example, generic testing instructions and sample test results were not sufficient evidence that the program actually worked. I needed to run the program and record the real results rather than claim that every test passed based only on an AI-generated checklist.

I also needed to adapt documentation examples to match the actual filenames, program behavior, repository details, and assignment requirements. Any suggested code or instructions that did not match my implementation would need to be changed or left out.

This helped ensure that the final submission represented the actual project rather than unverified AI-generated material.

## Verification

I was responsible for verifying the final project. AI-generated suggestions and documentation were not treated as proof that the program worked.

Verification included reviewing the code against the assignment requirements and checking the relevant program behavior, including:

- Loading inventory from the data file and handling a missing file.
- Displaying inventory items and summary information.
- Adding, updating, and removing inventory items.
- Rejecting invalid input, including negative quantities and empty required fields.
- Searching for items using case-insensitive, partial-name matching.
- Saving inventory changes and checking that the data file used the required format.
- Checking low-stock counts and category totals.
- Reviewing the README, testing documentation, and AI usage report for accuracy.

Actual test results should be recorded in `TESTING.md` after the corresponding tests have been performed. I should not mark a test as passed unless I have verified its result.

## Code Understanding

AI assistance focused primarily on explanations, documentation, and testing suggestions rather than replacing my implementation of the program's functions.

Two important parts of the project that I needed to understand were:

**1. Inventory search**

The search feature compares the user's search text with inventory item names without requiring an exact match. Case-insensitive matching allows searches such as `cable` to find an item named `USB-C Cable`. Partial matching makes the feature more flexible because users do not need to enter the complete item name. The program should also handle blank searches according to the assignment requirements.

**2. Inventory summary**

The summary feature calculates information from the current inventory list. It counts the number of unique inventory entries, adds their quantities to determine the total quantity, identifies items with quantities below five, and groups items by category. Category comparisons should ignore differences in capitalization so that variations in capitalization do not incorrectly create separate categories.

Understanding these operations helps me explain the program's behavior, evaluate whether the results are correct, and maintain the code independently.
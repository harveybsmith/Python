# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("raw_data", "budget_data_1.csv")
file_to_output = os.path.join("analysis", "budget_analysis_1.txt")

# Track various revenue parameters
total_months = 0
month_of_change = []
revenue_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_revenue = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to revenue_change_list
    first_row = next(reader)
    total_months = total_months + 1
    total_revenue = total_revenue + int(first_row[1])
    prev_revenue = int(first_row[1])

    for row in reader:

        # Track the total
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])

        # Track the revenue change
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row[0]]

        # Calculate the greatest increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
revenue_avg = sum(revenue_change_list) / len(revenue_change_list)

# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

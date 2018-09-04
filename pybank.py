import os
import csv


def fin_analysis(filename): 
    #use of remove to remove the header row 
    dataRows = []

    with open(filename, newline="") as File:
        budget_data_csv1 = csv.reader(File)
        for row in budget_data_csv1:
            dataRows.append(row)
    
    dataRows.remove(dataRows[0])
    # Declare variables
    revenue = []
    total_revenue = 0
    date = []
    months_count = 0
    rev_change = []
    avg_rev_change = 0

 # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in dataRows:
        #appends all the revenue values into its own array
        revenue.append(float(row[1]))
        #sums all those value with sum() funtion into a variable
        total_revenue = sum(revenue)
        #append all the months to an array
        date.append(row[0])
        #calculate the lenth of the months to a variable
        months_count = int(len(date))
    
    #print out results so far
    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", (months_count))
    print("Total Revenue: $", (total_revenue))

    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(rev_change)/len(rev_change)
        #now establish variables for the max and min revevue changes 
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)
        #create variable for the dates of the greatest increase and descrease
        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])
    
    #Now outside of for loop do the math operation to compute the Average revevue change, the months with greatest increase and decrease revenue change
    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

    # write results to a string and export to text file
    f = open('pybank.text', 'w')
    f.write((f'''
    Financial Analysis
    ----------------------------
    Total Months: {months_count}
    Total Revenue: {total_revenue}
    Average Revenue Change: {avg_rev_change}
    Greatest Increase in Revenue: Sep-16 {max_rev_change}
    Greatest Decrease in Revenue: Aug-12 {min_rev_change}
    '''
    ))
    f.close()


#call function for both files 
fin_analysis("budget_data_1.csv")
fin_analysis("budget_data_2.csv")

# # write results to a string and export to text file
# f = open('pybank.text', 'w')
# f.write((f'''
# Financial Analysis
# ----------------------------
# Total Months: {months_count}
# Total Revenue: {total_revenue}
# Average Revenue Change: {avg_rev_change}
# Greatest Increase in Revenue: Sep-16 {max_rev_change}
# Greatest Decrease in Revenue: Aug-12 {min_rev_change}
# '''
# ))
# f.close()
    
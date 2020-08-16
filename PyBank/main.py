import os
import csv
# Path to collect from Resources folder
budget_csv=os.path.join('..','PyBank','Resources','budget_data.csv')
#Declaring variables
total_months = 0
total_pl = 0
monthly_rev = 0
previous_rev = 0
revenue_change = 0
#Declaring Summary variables
total_rev_sum = int
average_rev_change = int
max_rev_change = int
min_rev_change = int
max_month_index = int
min_month_index = int
max_month = int
min_month = int
#Arrays to Summarize
revenue_changes = []
months = []
#read the csv file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next (csvreader)
    #Start to loop through data
    for row in csvreader:
        #add to total months and calculate monthly changes
        total_months = total_months + 1
        months.append(row[0])
        monthly_rev = int(row[1])
        total_pl = total_pl + monthly_rev
        if total_months > 1:
            revenue_change = monthly_rev + previous_rev
            revenue_changes.append(revenue_change)
        previous_rev = monthly_rev  
#Summarize the monthly results 
total_rev_sum = sum(revenue_changes)
average_rev_change = total_rev_sum / (total_months)-1
average_rev_change = round(average_rev_change, 2)
max_rev_change = max(revenue_changes, default=0)
min_rev_change = min(revenue_changes, default=0)
#Use index to find month for max and min
max_month_index = revenue_changes.index(max_rev_change)
min_month_index = revenue_changes.index(min_rev_change)
max_month = months[max_month_index]
min_month = months[min_month_index]
#print out Summary Results
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pl}")
print(f"Average Change: ${average_rev_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_rev_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_rev_change})")
#Create text file and export to analysis folder

pybank_output = os.path.join('..','PyBank','analysis',"pybankanalysis.txt")
with open (pybank_output, "w") as text:
    text.write("Financial Analysis" + "\n")
    text.write("--------------------------------"+ "\n")
    text.write(f"Total Months: {total_months}"+ "\n")
    text.write(f"Total: ${total_pl}"+"\n")
    text.write(f"Average Change: ${average_rev_change}"+ "\n")
    text.write(f"Greatest Increase in Profits: {max_month} (${max_rev_change})"+ "\n")
    text.write(f"Greatest Decrease in Profits: {min_month} (${min_rev_change})"+ "\n")

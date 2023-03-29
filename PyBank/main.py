import csv

file_path = "Resources/budget_data.csv"

#Total number of months
total_months=0

#The net total amount of "Profit/Losses" over the entire period
total = 0

#Profit and Losses list
changes = []

#months list
months = []

#CSV read + header
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csv_header)
    
    for row in csvreader:
        total_months = total_months +1
        total = total + int(row[1])
        changes.append(row[1])
        months.append(row[0])

        
#The changes in "Profit/Losses" over the entire period, and then the average of those changes    
substracts=[] # P/L current month - P/L previous month
for i in range(1, len(changes)):
    sub=int(changes[i]) - int(changes[i-1])
    substracts.append(sub)
    
sum_list=0 # Average of the changes
for i in range(len(substracts)):
    sum_list = int(sum_list) + int(substracts[i])
avg = round(sum_list/len(substracts),2)

#The greatest increase in profits (date and amount) over the entire period
max_profit = int(changes[0])
for i in changes:
    if int(i) > max_profit:
        max_profit = int(i)
index_max =changes.index(str(max_profit))
month_index_max=months[index_max]
#print("MAX MONTH", month_index_max)


#The greatest decrease in profits (date and amount) over the entire period
min_profit = int(changes[0])
for i in changes:
    if int(i) < min_profit:
        min_profit = int(i)
index_min=changes.index(str(min_profit))
month_index = months[index_min]
#print("MIN MONTH", month_index)


print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {month_index_max} (${max_profit})")
print(f"Greatest Decrease in Profits: {month_index} (${min_profit})")

# Set variable for output file
output_file = "Analysis/results.txt"


with open(output_file, "w") as file:
    file.write('\n')
    file.write("Financial Analysis ")
    file.write('\n')
    file.write('\n')
    file.write('\n')
    file.write(f"Total Months: {total_months}")
    file.write('\n')
    file.write(f"Total: ${total}")
    file.write('\n')
    file.write(f"Average Change: ${avg}")
    file.write('\n')
    file.write(f"Greatest Increase in Profits: {month_index_max} (${max_profit})")
    file.write('\n')
    file.write(f"Greatest Decrease in Profits: {month_index} (${min_profit})")
   

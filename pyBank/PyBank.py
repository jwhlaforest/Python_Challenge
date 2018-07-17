import os
import csv

#file path
csvpath = os.path.join('Resources','budget_data.csv')

#opening and reading the budget data
with open(csvpath, newline='') as csvfile:
    bud_data = csv.reader(csvfile, delimiter=',')
    next(bud_data)

    #variables
    total_months = 0
    total_net = 0
    loop = True
    last_diff = 0
    total_diff = 0
    last_month = 0
    average_change = 0
    inc_date = 0
    inc_diff = 0
    dec_date = 0
    dec_diff = 0

    #loop to calculate totals
    for line in bud_data:
        total_months = total_months + 1
        total_net = total_net + int(line[1])

        if loop == False:
            last_diff = last_month - int(line[1])
            total_diff = total_diff + last_diff
        last_month = int(line[1])

        if last_diff > inc_diff:
            inc_diff = last_diff
            inc_date = line[0]

        if last_diff < dec_diff:
            dec_diff = last_diff
            dec_date = line[0]

        loop = False

#total change / months
average_change = total_diff / (total_months)

print('Financial Analysis')
print('----------------------------')
print('Total Months:',total_months)
print('Total: $',total_net)
print('Average Change: $',average_change)
print('Greatest Increase in Profits:',inc_date,'($',inc_diff,')')
print('Greatest Decrease in Profits:',dec_date,'($',dec_diff,')')
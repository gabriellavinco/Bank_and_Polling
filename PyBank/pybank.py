import os 
import csv

csvpath=os.path.join('..','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")

    months = []
    revenue = []
    
    for row in csvreader:
        #print(row)
        #TOTAL MONTHS
        months.append(row[0])
        revenue.append(int(row[1]))
        total_months = len(months)
        #print(total_months)
       
       #TOTAL REVENUE
    total_revenue = sum(revenue)
    #print(total_revenue)

        #AVERAGE CHANGE
        #print(revenue)
    revenue_change = [revenue[i+1]-revenue[i] for i in range(len(revenue)-1)]
        #print(revenue_change)
    avg_change = sum(revenue_change)/float(len(revenue_change))
    avg_change = str(round(avg_change, 2))
        #print(avg_change)
        
        #GREATEST INCREASE
    profit_increase = max(revenue_change)
    k = revenue_change.index(profit_increase)
    month_increase = months[k+1]
    #print(month_increase)
    #print(profit_increase)

        #GREATEST DECREASE
    profit_decrease = min(revenue_change)
    j = revenue_change.index(profit_decrease)
    month_decrease = months[j+1]
    #print(month_decrease)
    #print(profit_decrease)
 

    #print functions
    output = ("Financial Analysis") + "\n"
    output += ("--------------------------------------") + "\n"
    output += (f"Total Months: {total_months}") + "\n"
    output += (f"Total: ${total_revenue}") + "\n"
    output += (f"Average Change: ${avg_change}") + "\n"
    output += (f"Greatest Increase in Profits: {month_increase} (${profit_increase})") + "\n"
    output += (f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})") + "\n"
    
    print(output)
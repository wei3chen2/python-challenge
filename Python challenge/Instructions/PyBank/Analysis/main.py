# To calculate the total number of months included in the dataset

# To calculate the net total amount of "Profit/Losses" over the entire period

# To calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes

# To calculate the greatest increase in profits (date and amount) over the entire period

# To calculate the greatest decrease in profits (date and amount) over the entire period


#import dependencies

import os
import csv


#path to the resources folder
#file = 'C:/Users/Stephanie/Desktop/Data analyst boot camp/Week 3-Python/Python challenge/Instructions/PyBank/Solved/budget_data.csv'

file = os.path.join(os.getcwd(),'budget_data.csv')


#Open CSV as Reader
with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    #create empty lists to add the csv values 
    month_count = []
    profit = []
    change_profit = []
    
                      
    #read the values 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
                      
#set up the max and min variable from the list made
increase = max(change_profit)
decrease = min(change_profit)

#using the index, 
month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      

output = os.path.join('C:/Users/Stephanie/Desktop/Data analyst boot camp/03-Python/Python challenge/Instructions/PyBank/Analysis', 'output.txt')
with open(output,"w") as book:
    book.write("Financial Analysis")
    book.write("\n")
    book.write("------------------------")
    book.write("\n")
    book.write(f"Total Months:{len(month_count)}")
    book.write("\n")
    book.write(f"Total: ${sum(profit)}")
    book.write("\n")
    book.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    book.write("\n")
    book.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    book.write("\n")
    book.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")





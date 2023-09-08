import os
import csv
import sys

budget_data_csv = "PyBank\\Resources\\budget_data.csv"

# Open and read csv
with open(budget_data_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    # Read the header row first (skip this part if there is no header)
    header=next(csv_reader)
    tot_num_rows=0
    profit=[]
    period=[]
    profit_change=[]
    tot_net=0

    #Iterating over the csv file to calculate total net profit/loss over entire period and total no. of rows
    for r in csv_reader:
        tot_net=tot_net+int(r[1])
        tot_num_rows=tot_num_rows+1
        #Adding all Date values to a list
        period.append(r[0])
        #Adding all profit/loss values to a list
        profit.append(float(r[1]))
        
    # Calculating the change in profit over the period and adding values to a list
    for i in range(1,len(profit)):
       profit_change.append(profit[i]-profit[i-1])
    
    average_change= sum(profit_change)/len(profit_change)
    max_prof_change=max(profit_change)
    # Calculating the index at which the max profit change occurs
    row_max_change=profit_change.index(max_prof_change)
   

    #Finding the corresponding period value at the index+1 position(profit_change has (tot_num_rows-1) number of values)
    per_max_change=period[row_max_change+1]
    min_pro_change=min(profit_change)

    # Calculating the index at which the min profit change occurs
    row_min_change=profit_change.index(min_pro_change)
    per_min_change=period[row_min_change+1]
    

# Defining function to print output statements, can be called to print output in terminal and text file.
def printing_output():
     print(f'Financial Analysis \n')
     print(f'--------------------------- \n')
     print(f'Total months :  {tot_num_rows}')      
     print(f'Total : ${tot_net}')
     print(f'Average: {average_change:.2f}')
     print(f'Greatest increase in Profits : {per_max_change} ({max_prof_change})')
     print(f'Greatest decrease in Profits: {per_min_change} ({min_pro_change})')

# Printing output to Terminal
printing_output()


# Writing all calculated values to text file named output.txt
stdoutOrigin=sys.stdout 
sys.stdout = open("PyBank\Resources\output.txt", "w")
printing_output()   
sys.stdout.close()
sys.stdout=stdoutOrigin
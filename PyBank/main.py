#bank

import os
import csv


#variables to calculate and zero down
tot_num_months = 0
net_tot_profit = 0
date_most_profit = "date_1"
date_most_loss = "date_2"
amt_most_profit = 0
amt_most_loss = 0
total_change = 0
average_change = 0

#variable for csv file
datafile = ["budget_data.csv"]


for file in datafile:
    csvpath = os.path.join("Resources","budget_data.csv")
    with open(csvpath, newline='') as csvfile:
        csvfile.readline()

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')


        #variables zeroed out again? I still don't understand why this has to happen to make it work...
        last_income = 0
        tot_num_months = 0
        net_tot_profit = 0
        amt_most_profit = 0
        amt_most_loss = 0

        #calculate variables
        for row in csvreader:
            net_tot_profit = net_tot_profit + int(row[1])
            tot_num_months = tot_num_months +1
            increased_value = int(row[1]) - last_income
            total_change = total_change + increased_value
            last_income =  int(row[1])
            if(increased_value > amt_most_profit):
                amt_most_profit = increased_value
                date_most_profit = row[0]
            
            if(increased_value < amt_most_loss):
                amt_most_loss = increased_value
                date_most_loss = row[0]

average_change = round(total_change/tot_num_months,2)

#text file save to
outputpath = os.path.join("Resources",file.split(".")[0] + "_Results.txt")
lines = []
resultsfile = open(outputpath, "w")
    


#text file structure from example
lines.append("Financial Analysis")
lines.append("--------------")
lines.append("Total Months : "+str(tot_num_months))
lines.append("Total : " + str(net_tot_profit))
lines.append("Average Chang : "+str(average_change))
lines.append("Greatest Increase in Profits : "+date_most_profit + " $" + str(amt_most_profit) +")")
lines.append("Greatest Decrease in Profits : "+date_most_loss + " $" + str(amt_most_loss) +")")


#finish the output
for line in lines:

    print(line)

    print(line,file=resultsfile)
        
print()
    
#end writing to file
resultsfile.close()
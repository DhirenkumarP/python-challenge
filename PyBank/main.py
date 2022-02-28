import os
import csv

total_months = 0
total = 0
average_change = 0
previous_change = 0
average_list=[]
monthly_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

pybank_csv = os.path.join('..', 'Resources', 'budget_data.csv')
with open(pybank_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        total_months = total_months + 1
        total = total + int(row[1])

        average_change = int(row[1])- previous_change
        previous_change = int(row[1])
        average_list = average_list + [average_change]
        monthly_change = [monthly_change] + [row[0]]

        
        if average_change > greatest_increase[1]:
            greatest_increase[1] = average_change
            greatest_increase[0] = row[0]

        if average_change < greatest_decrease[1]:
            greatest_decrease[1] = average_change
            greatest_decrease[0] = row[0]

        

    average_change = round(sum(average_list)/len(average_list),2)

    print("Financial Analysis")
    print("---------------------------------------------------------")
    print("Total Months: " + str(total_months))
    print("Total : " + "$" + str(total))
    print("Average Change: " + "$" + str(average_change))
    print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) +")")
    print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) +")")

output_path = os.path.join("output.txt")
with open(output_path, "w") as txt_file:
    

    txt_file.write("..", "analysis", "Financial Analysis")
    txt_file.write("\n")
    txt_file.write("---------------------------------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total : " + "$" + str(total))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(average_change))
    txt_file.write("\n")
    txt_file.write("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) +")")
    txt_file.write("\n")
    txt_file.write("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) +")")
    txt_file.write("\n")
    


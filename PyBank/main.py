import pandas as pd
import os

budget_data_csv_path = "Resources/budget_data.csv"
budget_data_df = pd.read_csv(budget_data_csv_path, encoding="utf8")
budget_data_df.head()


totalmonths = len(budget_data_df['Date'])
print(totalmonths)

sumprofit = budget_data_df['Profit/Losses'].sum()
print(sumprofit)

change_df = budget_data_df['Profit/Losses'].diff()
print(change_df)


avgchange_df = change_df.mean()
print(avgchange_df)


max_change_df = change_df.max()
min_change_df = change_df.min()

print(max_change_df)
print(min_change_df)
print('Financial Analysis')
print()
print('-----------------------')
print()
print('Total Months: ' + str(totalmonths))
print()
print('Total: ' + str(sumprofit))
print()
print('Average Change: ' + str(avgchange_df))
print()
print('Greatest Increase in Profits: ' + str(max_change_df))
print()
print('Greatest Decrease in Profits: ' +str( min_change_df)) 

# export to file
output_file = os.path.join('output.csv')
with open(output_file, 'w') as datafile
    writer = csv.writer(datafile)
    writer.writerow(["Total Months", "Total", "Average Change", "Greatest Increase", "Greatest Decrease"])
    writer.writerows(totalmonths, + sumprofit, + avgchange_df, + max_change_df, + min_change_df)

# import dependencies
import os
import csv
import pandas as pd
import numpy as np

# find and extract csv file
election_data_csv_path = 'Resources/election_data.csv'
election_data_df = pd.read_csv(election_data_csv_path, encoding='utf8')

# determine number of votes cast
totesvotes = len(election_data_df['Ballot ID'])
#determine names using unique value function
candidate_list = np.unique(election_data_df['Candidate'])
# number of votes per candidate
votecount = election_data_df['Candidate'].value_counts()
allvotes = sum(election_data_df['Candidate'].value_counts())candidate1 = election_data_df['Candidate'].value_counts()/allvotes

# zip row for output
results = zip (candidate_list, candidate1, votecount)

# print results to terminal
print('Election Results')
print('---------------------')
print()
print(votecount, candidate1[-0])
print()
print(candidate1)
print()
print()
print('--------------------')
print(f'The winner is {votecount[0]}')

#export results to file
output_file = os.path.join("output.csv")
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Name", "Percentage", "Total Votes"])
    writer.writerows(results)
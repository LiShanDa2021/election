#What we need
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. Winner based on popular vote

#1. Total number of votes cast
#   find the number of rows
#   store this to a variable

#2. A complete list of candidates
#   Loop through all rows
#   Maybe when the candidate doesn't match the candidate the next row down, store that candidate to string 
#   and append it to a list

#3. Total number of votes a candidate receives
#   when determining the existing candidates, keep a variable that stores the number of times that name appears

#4. percentage of votes cast
#   you know

import datetime as dt

now = dt.datetime.now()

print(now)

#add dependencies
import csv
import os

#create file variable to load
file_to_load = os.path.join('resources', 'election_results.csv')

#create filename variable to save
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total vote counter
total_votes = 0

#initialize candidate list
candidate_options = []
#initialize dictionary to map candidates to vote count
candidate_votes = {}

#initialize winning candidate, winning_count and winning_percentage tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:

    #read the file object with the reader function
    file_reader  = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #increase total vote count
        total_votes += 1
        #print(row)
        #find candidate name
        candidate_name = row[2]
        #determine if candidate is not in list, add candidate if not yet added to list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #increase candidate vote count
        candidate_votes[candidate_name] += 1


#print total number of votes
print(candidate_votes)
print(f"Total Votes = {total_votes}")

#find percentage of vote
for candidate_name in candidate_votes:
    vote_percentage = (float(candidate_votes[candidate_name]) / float(total_votes)) * 100
    print(f"{candidate_name} earned {vote_percentage:.1f}% of the vote.")
    #determine if candidate has the winning count, set winning totals if true
    if candidate_votes[candidate_name] > winning_count and vote_percentage > winning_percentage:
        winning_candidate = candidate_name
        winning_count = candidate_votes[candidate_name]
        winning_percentage = vote_percentage

print("")

#print winning candidate
print(f"{winning_candidate} is the winner with {winning_count} votes and {winning_percentage:.1f}% of the vote")

#open the file to write
with open(file_to_save, 'w') as txt_file:

    #write some data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")










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

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #read the file object with the reader function
    file_reader  = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)
    print(headers)

    #print each row in the csv file
    #for row in file_reader:
        #print(row)

#open the file to write
with open(file_to_save, 'w') as txt_file:

    #write some data to the file
    txt_file.write("Counties in the Election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\n")
    txt_file.write("Denver\n")
    txt_file.write("Jefferson\n")










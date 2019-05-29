#election

import os
import csv

#set variables to calculate and zero down
candidates = []
num_votes = 0
vote_counts = []


#variable for csv file
datafile = ["election_data.csv"]


for file in datafile:
    csvpath = os.path.join("Resources","election_data.csv")
    with open(csvpath, newline='') as csvfile:
        csvfile.readline()

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        #count up the votes by row
        for row in csvreader:

            #add up the rolling total
            num_votes = num_votes + 1

            #candidate voted for
            candidate = row[2]

            #if the candidate has more votes then add to the total
            if candidate in candidates:
                candidate_index = candidates.index(candidate)
                vote_counts[candidate_index] = vote_counts[candidate_index] + 1
            #else (otherwise) make a new candidate to tally in the list
            else:
                candidates.append(candidate)
                vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0

#calculations for the winner and percentages
for count in range(len(candidates)):
    vote_percentage = round(vote_counts[count]/num_votes*100,5)
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

#text file save to
outputpath = os.path.join("Resources",file.split(".")[0] + "_Results.txt")
lines = []
resultsfile = open(outputpath, "w")
    


#text file structure from example
lines.append("Election Results")
lines.append("--------------")
lines.append("Total Votes : "+str(num_votes))
lines.append("--------------")
for count in range(len(candidates)):
     lines.append(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
lines.append("--------------")
lines.append(f"Winner: {winner}\n")
lines.append("--------------")


#finish the output
for line in lines:

    print(line)

    print(line,file=resultsfile)
        
print()
    
#end writing to file
resultsfile.close()
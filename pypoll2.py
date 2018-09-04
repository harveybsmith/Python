import os
import csv

election_data = []

csvpath = os.path.join('election_data_1.csv')
#csvpath2 = os.path.join('election_data_2.csv')

with open(csvpath, newline="") as File:
    election_data_csv1 = csv.reader(File, delimiter= ',')
    for row in election_data_csv1:
        election_data.append(row)

# define variables
voteTally = 0
total_votes = 0
candidates = []
individuals = []
votes_per_cand = 0

election_data.remove(election_data[0])

#The total number of votes cast
total_votes = int(len(election_data))
print(total_votes)

"""
To make a list fo candidates who recieved votes 
"""
#Run for loop to make raw list of candidates who recieved votes
for row in election_data:
    candidates.append(row[2])
    if row[2] in individuals:
        idx = individuals.index(row[2])
        voteTally += 1
    else: 
        individuals.append(row[2])

print(individuals)

#Now create count funtion to count the occurance of each candidate from the list of candidates 
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count

#create variable for the vote count for each candidate, calling the count funciton
countVestal = countX(candidates, "Vestal")
countTorres = countX(candidates, "Torres")
countSeth = countX(candidates, "Seth")
cordinCount= countX(candidates, "Cordin")

winner = "Vestal"

#Calculate the percentage each of votes each candidate won
perVestal = float((countVestal / total_votes) * 100)
perTorres = float((countTorres / total_votes) * 100)
perSeth = float((countSeth / total_votes) * 100)
perCordin = float((cordinCount / total_votes) * 100) 

# format a long string to export as a text file
#write code to text file with the open() funtion
#output_path = os.path.join("pypoll_results.txt")

f = open('pypoll.text', 'w')
f.write((f'''Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
Vestal: {perVestal}%  ({countVestal})
Torres: {perTorres}%  ({countTorres})
Seth: {perSeth}%  ({countSeth})
Cordin: {perCordin}%  ({cordinCount})
-------------------------
Winner: {winner}
-------------------------'''))
f.close()


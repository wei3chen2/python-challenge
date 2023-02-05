#To calculate the total number of votes cast

#To calculate a complete list of candidates who received votes

#To calculate the percentage of votes each candidate won

#To calculate the total number of votes each candidate won

#To calculate the winner of the election based on popular vote.



#import dependencies

import os
import csv

file = os.path.join("C:/Users/Stephanie/Desktop/Data analyst boot camp/03-Python/Python challenge/Instructions/PyPoll/Resources/",'election_data.csv')


#open and read csv

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")
    csv_header = next(csv_file)
    print(f"Header:{csv_header}")
    

#Set up Variables
    votescast=0
    totalvotescast=0
    candidates=[]
    numberwon = {}
    percentwon=0
    winnername=""
    winnervotes=0
  
#The total number of votes cast

    for row in csv_reader:
        votescast +=1
    
#A complete list of candidates who received votes
#The total number of votes each candidate won
        for i in range(2,3):
            if row[i] not in candidates:
                candidates.append(row[i])
                numberwon[row[i]]=0
            numberwon[row[i]]+=1
        
#Print
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {votescast}")
print(f"-------------------------")


#The percentage of votes each candidate won
for name in numberwon:
    votes = numberwon[name]
    percentage = votes / votescast
    pretty = percentage * 100
    print(f"{name}: {pretty:.3f}% ({votes})")
    #The winner of the election based on popular vote.
    if votes > winnervotes: 
        winnervotes = votes
        winnername = name
    #Print 
print(f"-------------------------")
print(f"Winner: {winnername}")
print(f"-------------------------")


output = open("C:/Users/Stephanie/Desktop/Data analyst boot camp/03-Python/Python challenge/Instructions/PyPoll/Analysis/file.txt","w")

output.write(f"Header:{csv_header}\n")

output.write(f"Election Results\n")
output.write(f"-------------------------\n")
output.write(f"Total Votes: {votescast}\n")
output.write(f"-------------------------\n")

for name in numberwon:
    votes = numberwon[name]
    percentage = votes / votescast
    pretty = percentage * 100
    output.write(f"{name}: {pretty:.3f}% ({votes})\n")


output.write(f"-------------------------\n")
output.write(f"Winner: {winnername}\n")
output.write(f"-------------------------\n")

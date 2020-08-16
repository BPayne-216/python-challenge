import os
import csv
# Path to collect from Resources folder
poll_csv=os.path.join('..','PyPoll','Resources','election_data.csv')
#Declaring variables
total_votes_count = 0
j = 0
#Arrays to Summarize
votes = []
candidatevotes = []
subcandidates = []
votepercentages = []
#read the csv file
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader)
    #Start to loop through data
    for row in csvreader:
        #counts total number of votes
        total_votes_count = total_votes_count + 1
        #if goes through the candidate votes
        if row[2] not in subcandidates:
            subcandidates.append(row[2])
        #makes list of all votes    
        votes.append(row[2])
    #Calculates the candidate votes and the percentage of votes for candidate
    for sub in subcandidates:
        subcandidates.append(votes.count(sub))
        votepercentages.append(round(votes.count(sub)/total_votes_count*100,3))
    #Go through the candidate subs and find the winner by max
    winner = subcandidates(candidatevotes.index(max(candidatevotes))

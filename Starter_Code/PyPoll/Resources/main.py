import csv
import sys
import os

election_data_csv = "PyPoll\\Resources\\election_data.csv"
# Open and read csv
with open(election_data_csv, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    header=next(csv_reader)
    tot_num_votes=0
    candidates_list=[]
    unique_candidates=[]
    vote_count_candidate=[]
    vote_percent_candidate=[]

    # Calculating the total number of votes by counting total rows of data. Adding all candidates names(Candidate) to a list
    for r in csv_reader:
        tot_num_votes=tot_num_votes+1
        candidates_list.append(r[2])
    
    # Finding unique candidates in the Election
    for i in candidates_list:
        if i not in unique_candidates:
            unique_candidates.append(i)
    
    # Calculating the vote count for each unique Candidate and adding values to list 
    for i in unique_candidates:
        count_votes=candidates_list.count(i)
        vote_count_candidate.append(count_votes)
        percent_vote=(count_votes/tot_num_votes)
        vote_percent_candidate.append(percent_vote)
    
    
    # Finding the Winner
    for i in range(1,len(vote_count_candidate)):
        if vote_count_candidate[i]>vote_count_candidate[i-1]:
            winner=unique_candidates[i]
    
    # Defining function to print output statements, can be called to print output in terminal and text file.
    def printing_output():
        print(f'Election Results \n')
        print(f'--------------------------- \n')
        print(f'Total Votes :  {tot_num_votes}')
        print(f'--------------------------- \n')
        for i in range(0, len(unique_candidates)):
            print(f'{unique_candidates[i]} : {vote_percent_candidate[i]:.3%} ({vote_count_candidate[i]})')
        print(f'--------------------------- \n')
        print(f'Winner : {winner}')
        print(f'--------------------------- \n')

# Printing output to Terminal
printing_output()

# Writing all calculated values to text file named output.txt
stdoutOrigin=sys.stdout 
sys.stdout = open("PyPoll\Resources\output.txt", "w")
printing_output()   
sys.stdout.close()
sys.stdout=stdoutOrigin
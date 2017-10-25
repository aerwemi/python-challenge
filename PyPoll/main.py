# import os and csv lib to load data 
import os
import csv

#input file name - to be used later for other files in same dir location 
file_name=input("Input Voter File (*.csv):")

# for file location 
Vote_data = os.path.join("raw_data", file_name)


# open the file and loop over the fhd, update Revenue=[] and Months=[]

Candidates=[]

with open(Vote_data, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Skip csv headers  
    next(csv_reader, None)

    # Loop over fh
    for row in csv_reader:
        Candidates.append(row[2]) # Update candidate list


# finding vote summary
total_votes=len(Candidates)
cand_list=set(Candidates)
cand_list=[i for i in cand_list]
vote_counts=[Candidates.count(i) for i in cand_list]
vote_percent= [((Candidates.count(i)/total_votes)*100) for i in cand_list]
vote_percent= [round(i,3) for i in vote_percent]

max_vote=max(vote_counts)


mx,idx = max( (vote_counts[i],i) for i in range(len(vote_counts)) )

wins=cand_list[idx]
        
    
# printing vote summary    
print('Election Results')
print('-------------------------')
print('Total Votes: ' + str(total_votes) )
print('-------------------------')

cand_num=0
for i in cand_list:
    print(i + ': ' + str(vote_percent[cand_num])+'% '+ '(' + str(vote_counts[cand_num]) + ')' )
    cand_num+=1

print('-------------------------')

print('Winner: ' + str(wins)) 

print('-------------------------')
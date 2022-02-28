import os
import csv

total_votes = 0
winner_votes = 0
total_candidates = 0
candidates = []
candidate_votes = {}
greatest_votes = ["", 0]

pypoll_csv = os.path.join('election_data.csv')
with open(pypoll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        total_candidates = row[2]

        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 1

        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1

    if (total_votes > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row[2]

        print("Election Results")
        print("-----------------------------------------")
        print("Total Votes: " + str(total_votes))
        print("-----------------------------------------")

        for candidate in candidate_votes:
            print(candidate + " : " + str((candidate_votes[candidate]/total_votes)*100) + "%" + " (" + str(candidate_votes[candidate]) + ")")
            
            winner = sorted(candidates)

        print("-----------------------------------------")
        print("Winner: " + str(winner[1]))
        print("-----------------------------------------")
          
output_path = os.path.join("output.txt")
with open(output_path, "w") as txt_file:


    txt_file.write("Election Result")
    txt_file.write("\n")
    txt_file.write("------------------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes: " + str(total_votes))
    txt_file.write("\n")
    txt_file.write("------------------------------------")
    txt_file.write("\n")
    for candidate in candidate_votes:
        txt_file.write(candidate + " : " + str((candidate_votes[candidate]/total_votes)*100) + "%" + " (" + str(candidate_votes[candidate]) + ")""\n")
    txt_file.write("-----------------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[1]))
    txt_file.write("\n")

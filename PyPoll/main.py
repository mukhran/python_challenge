import csv

csvpath = "Resources/election_data.csv"
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #header row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    #Total number of votes cast
    total_votes = 0
    
    #list of candidate
    unique = []
    Charles = 0
    Diana = 0
    Raymon = 0

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in unique:
            unique.append(row[2])
    

        if row[2] == "Charles Casper Stockham":
            Charles +=1
        elif row[2] == "Diana DeGette":
            Diana +=1
        elif row[2] == "Raymon Anthony Doane":
            Raymon +=1

    per_charles = round(Charles*100/total_votes,2)
    per_diana = round(Diana*100/total_votes,2)
    per_raymon = round(Raymon*100/total_votes,2)


    print(f"Total Votes: {total_votes}")
    print(unique)
    print(f"Charles Casper Stockham: {per_charles}% ({Charles})") 
    print(f"Diana DeGette: {per_diana}% ({Diana})")
    print(f"Raymon Anthony Doane: {per_raymon}% ({Raymon})")

    winner = max(Charles, Diana, Raymon)
    print(f"Winner: {winner}")

    # Set variable for output file
    output_file = "Analysis/results.txt"


    with open(output_file, "w") as file:
        file.write('\n')
        file.write("Election Results ")
        file.write('\n')
        file.write("----------------------------------------------------------------")
        file.write('\n')
        file.write('\n')
        file.write(f"Total Votes: {total_votes}")
        file.write('\n')
        file.write("-----------------------------------------------------------------")
        file.write('\n')
        file.write('\n')
        file.write(f"Charles: {per_charles}% ({Charles})")
        file.write('\n')
        file.write((f"Diana DeGette: {per_diana}% ({Diana})"))
        file.write('\n')
        file.write(f"Raymon Anthony Doane: {per_raymon}% ({Raymon})")
        file.write('\n')
        file.write("-----------------------------------------------------------------")
        file.write('\n')
        file.write('\n')
        file.write((f"Winner: Diana DeGette {winner}"))





    

    
        
        
    



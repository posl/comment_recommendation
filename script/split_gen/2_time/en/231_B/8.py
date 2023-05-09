def main():
    #get the number of people who voted
    num_people = int(raw_input())
    #get the list of names from the input
    names = [raw_input() for i in range(num_people)]
    #sort the list of names
    names.sort()
    #get the list of unique names
    unique_names = list(set(names))
    #get the number of unique names
    num_unique_names = len(unique_names)
    #get the list of the number of votes for each unique name
    num_votes = [names.count(unique_names[i]) for i in range(num_unique_names)]
    #get the index of the name with the most votes
    index_most_votes = num_votes.index(max(num_votes))
    #print the name with the most votes
    print unique_names[index_most_votes]

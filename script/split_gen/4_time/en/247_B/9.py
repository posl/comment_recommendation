def problem():
    #Get the number of people
    number_of_people = int(input())
    #Get the names of the people
    people_names = []
    for i in range(number_of_people):
        people_names.append(input().split())
    #Check if the names are valid
    for i in range(number_of_people):
        if people_names[i][0] in people_names[i][1:]:
            print("Yes")
            return
        elif people_names[i][1] in people_names[i][0:i] or people_names[i][1] in people_names[i][i+1:]:
            print("Yes")
            return
    print("No")
    return
problem()

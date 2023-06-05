def problem247_b():
    n = int(input())
    people = []
    for i in range(n):
        people.append(input().split())
    for i in range(n):
        for j in range(n):
            if i != j:
                if people[i][0] == people[j][0] or people[i][1] == people[j][1]:
                    print("Yes")
                    return
    print("No")

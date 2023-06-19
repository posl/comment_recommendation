def main():
    N = int(input())
    people = []
    for i in range(N):
        people.append(list(map(int,input().split())))
    S = input()
    for i in range(N):
        if S[i] == 'R':
            people[i][0] += 1
        elif S[i] == 'L':
            people[i][0] -= 1
    print(people)
    for i in range(N):
        for j in range(i+1,N):
            if people[i][0] == people[j][0] and people[i][1] == people[j][1]:
                print('Yes')
                return
    print('No')

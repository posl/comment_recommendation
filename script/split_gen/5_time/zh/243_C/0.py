def main():
    N = int(input())
    people = []
    for i in range(N):
        people.append(list(map(int, input().split())))
    direction = input()
    #print(N, people, direction)
    #print(people[0][0])
    #print(people)
    for i in range(N):
        if direction[i] == 'R':
            people[i][0] += 1
        else:
            people[i][0] -= 1
    #print(people)
    people.sort()
    #print(people)
    for i in range(N-1):
        if people[i][0] == people[i+1][0] and people[i][1] == people[i+1][1]:
            print('Yes')
            exit()
    print('No')

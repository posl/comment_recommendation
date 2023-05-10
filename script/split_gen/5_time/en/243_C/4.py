def main():
    N = int(input())
    people = []
    for i in range(N):
        people.append(list(map(int, input().split())))
    S = input()
    collision = False
    for i in range(N):
        if S[i] == 'R':
            for j in range(i+1,N):
                if S[j] == 'L':
                    if people[i][1] == people[j][1]:
                        if (people[i][0] + people[j][0]) % 2 == 0:
                            collision = True
                            break
    if collision:
        print('Yes')
    else:
        print('No')

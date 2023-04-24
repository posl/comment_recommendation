Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    ans = ['No'] * N
    for i in range(N):
        if S[i] in T:
            ans[i] = 'Yes'
    print(*ans, sep='

')
    return

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    ans = [0] * N
    for i in range(N):
        if S[i] in T:
            ans[i] = 1
    for i in range(N):
        if ans[i] == 1:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    ans = ['No']*n
    for i in range(n):
        if s[i] in t:
            ans[i] = 'Yes'
    print('

'.join(ans))

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    S_set = set(S)
    T_set = set(T)
    if S_set & T_set:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    express = [False] * N
    for i in range(M):
        express[S.index(T[i])] = True
    for i in range(N):
        if express[i]:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    express = []
    for t in T:
        for i in range(N):
            if t == S[i]:
                express.append(i)
    for i in range(N):
        if i in express:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    N,M = map(int,input().split())
    S = input().split()
    T = input().split()
    #print(N,M)
    #print(S)
    #print(T)
    #print("----")
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 10

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()

    # 1. Create a list of 0s
    # 2. Loop through the list
    # 3. If the station is in the express train list, set the value to 1
    # 4. Print Yes if the value is 1, No if the value is 0
    station_list = [0] * n
    for i in range(n):
        if s[i] in t:
            station_list[i] = 1

    for i in range(n):
        if station_list[i] == 1:
            print("Yes")
        else:
            print("No")

main()

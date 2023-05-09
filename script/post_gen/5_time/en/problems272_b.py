Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    parties = []
    for i in range(M):
        parties.append(list(map(int, input().split()))[1:])
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for party in parties:
                if i+1 not in party or j+1 not in party:
                    break
            else:
                print("Yes")
                return
    else:
        print("No")

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    l = []
    for i in range(m):
        l.append(list(map(int, input().split()))[1:])
    for i in range(m):
        for j in range(i+1, m):
            if len(set(l[i]+l[j])) == len(l[i])+len(l[j]):
                print("NO")
                return
    print("YES")

=======
Suggestion 3

def solve():
    N, M = map(int, input().split())
    parties = []
    for _ in range(M):
        parties.append(set(map(int, input().split()[1:])))
    for i in range(M):
        for j in range(i+1, M):
            if parties[i] & parties[j]:
                parties[i] |= parties[j]
                parties[j] = set()
    if all(parties):
        print("Yes")
    else:
        print("No")
solve()

=======
Suggestion 4

def main():
    n,m = map(int, input().split())
    x = []
    for _ in range(m):
        x.append(list(map(int, input().split()))[1:])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            for k in range(m):
                if not (i+1 in x[k] and j+1 in x[k]):
                    break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print("Yes")
        return
    print("No")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    k = []
    x = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(m):
        for j in range(m):
            if i != j:
                if len(set(x[i]) & set(x[j])) > 0:
                    x[i] = list(set(x[i]) | set(x[j]))
    if len(set(x[0])) == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    N,M = map(int, input().split())
    x = []
    for i in range(M):
        x.append(list(map(int, input().split()))[1:])

    for i in range(N):
        for j in range(i+1,N):
            if not (i+1 in x[j-i-1]):
                print("No")
                return
    print("Yes")

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    k = []
    x = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    print('Yes' if len(set(x[0]) & set(x[1])) > 0 else 'No')

=======
Suggestion 8

def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split()))[1:] for _ in range(M)]
    ans = 'No'
    for i in range(N):
        for j in range(i+1, N):
            if all(i+1 in x and j+1 in x for x in S):
                ans = 'Yes'
    print(ans)

main()

=======
Suggestion 9

def main():
    n,m = map(int,input().split())
    x = []
    for i in range(m):
        x.append(list(map(int,input().split())))
    for i in range(1,n+1):
        if x[0][0] in x[i-1][1:]:
            if x[i-1][0] in x[0][1:]:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 10

def check_attendees(attendees):
    for i in range(len(attendees)):
        for j in range(i+1,len(attendees)):
            if attendees[i] == attendees[j]:
                return True
    return False

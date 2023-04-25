Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(len([d for d in D if d <= X]))

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    print(sum(1 for d in D if d <= X))

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[-1] + L[i])
    count = 0
    for i in range(N+1):
        if D[i] <= X:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(1, N+1):
        D.append(D[i-1]+L[i-1])
    print(len([d for d in D if d <= X]))

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    D = [0]
    for i in range(N):
        D.append(D[i] + L[i])
    ans = 0
    for i in range(N+1):
        if D[i] <= X:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    d = [0]
    for i in range(N):
        d.append(d[i] + L[i])
    print(sum([1 for i in d if i <= X]))

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    ans = 0
    d = 0
    for i in range(N+1):
        if d <= X:
            ans += 1
        d += L[i]
    print(ans)

main()

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    L = list(map(int, input().split()))
    locations = [0]
    for i in range(N):
        locations.append(locations[i] + L[i])
    print(sum([1 for i in locations if i <= X]))

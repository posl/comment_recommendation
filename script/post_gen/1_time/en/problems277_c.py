Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if N % 2 == 0:
        print(B[N // 2] - A[N // 2] + 1)
    else:
        print(B[N // 2] - A[N // 2] + 1)

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    if N % 2 == 0:
        ans = (B[N // 2] - A[N // 2] + 1) + (B[N // 2 - 1] - A[N // 2 - 1] + 1) - 1
    else:
        ans = B[N // 2] - A[N // 2] + 1

    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    maxA = max(A)
    maxB = max(B)
    if maxA > maxB:
        print(maxA)
    else:
        print(maxB)

=======
Suggestion 4

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(list(map(int, input().split())))
    ladders.sort(key=lambda x: x[1], reverse=True)
    current = 1
    for ladder in ladders:
        if ladder[0] <= current <= ladder[1]:
            current = ladder[1]
        elif ladder[1] <= current <= ladder[0]:
            current = ladder[0]
    print(current)

=======
Suggestion 5

def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(tuple(map(int, input().split())))
    ladders.sort(key=lambda x: x[0])
    print(ladders[-1][1])

main()

=======
Suggestion 6

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline

    N = int(input())
    ladder = []
    for _ in range(N):
        A, B = map(int, input().split())
        ladder.append((min(A, B), max(A, B)))

    ladder.sort(key=lambda x: x[0])
    max_floor = ladder[-1][1]
    ladder_dict = defaultdict(list)
    for A, B in ladder:
        ladder_dict[A].append(B)

    dp = [0] * (max_floor + 1)
    for i in range(1, max_floor + 1):
        if i in ladder_dict:
            for j in ladder_dict[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    print(dp[-1])

=======
Suggestion 7

def main():
    N = int(input())
    ladders = []
    for _ in range(N):
        ladders.append(tuple(map(int, input().split())))
    ladders.sort(key=lambda x: x[1])
    now = 1
    for i in range(N):
        if ladders[i][0] <= now:
            now = ladders[i][1]
        elif ladders[i][1] <= now:
            now = ladders[i][0]
    print(now)

=======
Suggestion 8

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)

    #A,Bのうち大きい方を採用
    #A,Bのうち小さい方を採用
    #A,Bのうちどちらかを採用
    #A,Bのうちどちらも採用

    #A,Bのうち大きい方を採用
    #A,Bのうち小さい方を採用
    #A,Bのうちどちらかを採用
    #A,Bのうちどちらも採用

    #A,Bのうちどちらも採用
    #A,Bのうちどちらかを採用
    #A,Bのうち小さい方を採用
    #A,Bのうち大きい方を採用

    #A,Bのうちどちらかを採用
    #A,Bのうちどちらも採用
    #A,Bのうち大きい方を採用
    #A,Bのうち小さい方を採用

    #A,Bのうち小さい方を採用
    #A,Bのうちどちらかを採用
    #A,Bのうちどちらも採用
    #A,Bのうち大きい方を採用

    #A,Bのうち大きい方を採用
    #A,Bのうちどちらかを採用
    #A,Bのうちどちらも採用
    #A,Bのうち小さい方を採用

    #A,Bのうちどちらも採用
    #A,Bのうちどちらかを採用
    #A,Bのうち大きい方を採用
    #A,Bのうち小さい方を採用

    #A,Bのうちどちらかを採用
    #A,Bのうち

=======
Suggestion 9

def main():
    from sys import stdin
    from collections import defaultdict

    def input():
        return stdin.readline().strip()

    N = int(input())
    ladders = []
    for i in range(N):
        A, B = map(int, input().split())
        ladders.append((A, B))

    # Sort the ladders by their starting point
    ladders.sort()

    # Set of the floors that can be reached
    reached = set()

    # Set of the floors that can be reached by using the ladders that have already been used
    reached_by_used_ladders = set()

    # Set of the floors that can be reached by using the ladders that have not been used
    reached_by_unused_ladders = set()

    # Add the starting floor
    reached.add(1)
    reached_by_unused_ladders.add(1)

    # Iterate through the ladders
    for A, B in ladders:
        # Check if the ladder can be used
        if A in reached_by_unused_ladders or B in reached_by_unused_ladders:
            # Add the floors that can be reached by using this ladder
            reached.add(A)
            reached.add(B)
            reached_by_used_ladders.add(A)
            reached_by_used_ladders.add(B)
            # Remove the floors that can be reached by using the ladders that have not been used
            reached_by_unused_ladders.difference_update(reached_by_used_ladders)

    # Print the answer
    print(max(reached))

=======
Suggestion 10

def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int,input().split())))
    ab.sort(key=lambda x: x[0])
    #print(ab)
    ans = 1
    for i in range(n):
        if ans < ab[i][0]:
            break
        ans = ab[i][1]
    print(ans)

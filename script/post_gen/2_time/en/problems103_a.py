Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[1] - A[0] + A[2] - A[1])

main()

=======
Suggestion 2

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(A[1] - A[0] + A[2] - A[1])

=======
Suggestion 3

def main():
    A = list(map(int, input().split()))
    print(min(abs(A[0]-A[1])+abs(A[1]-A[2]), abs(A[0]-A[2])+abs(A[1]-A[2])))

=======
Suggestion 4

def main():
    A = list(map(int, input().split()))
    A.sort()
    print(abs(A[0] - A[1]) + abs(A[1] - A[2]))

=======
Suggestion 5

def main():
    A = list(map(int, input().split()))
    ans = 0
    for i in range(1, len(A)):
        ans += abs(A[i] - A[i - 1])
    print(ans)

=======
Suggestion 6

def main():
    A = [int(i) for i in input().split()]
    A.sort()
    print(A[2]-A[0])

=======
Suggestion 7

def main():
    A = list(map(int, input().split()))
    print(max(A) - min(A))

=======
Suggestion 8

def min_cost(costs):
    costs.sort()
    return costs[1] - costs[0] + costs[2] - costs[1]

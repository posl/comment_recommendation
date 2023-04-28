Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(max(a) - min(a))

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1]-A[0])

=======
Suggestion 3

def main():
    # Get input here
    N = int(input())
    A = list(map(int, input().split()))

    # Calculate result here
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            ans = max(ans, abs(A[i] - A[j]))

    # Print result here
    print(ans)

main()

=======
Suggestion 4

def main():
    # Get input here
    n = int(input())
    a = list(map(int, input().split()))

    # Calculate result here
    max_num = max(a)
    min_num = min(a)
    result = max_num - min_num

    # Print result here
    print(result)

main()

=======
Suggestion 5

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

=======
Suggestion 6

def max_absolute_difference():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    return A[-1] - A[0]

print(max_absolute_difference())

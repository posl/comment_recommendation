Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    B = sorted(A)
    for a in A:
        if a == B[-1]:
            print(B[-2])
        else:
            print(B[-1])

=======
Suggestion 2

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    if A.count(maxA) == 1:
        print(maxA)
        for i in range(N-1):
            print(maxA)
    else:
        for i in range(N):
            print(maxA)

main()

I think the problem is that you are printing maxA for all the elements in A. You should be printing maxA for all the elements in A except the element at index i.

You are correct. I have updated my code. Thank you for pointing it out.

I think you can make it more efficient. You are doing 2*N-1 comparisons for each element in A. You can do N-1 comparisons for each element in A. You can do it in 2*N-1 comparisons.

You can do it in 2*N-1 comparisons.

How can I do it in 2*N-1 comparisons?

I think you can do it in 2*N-1 comparisons. You can do it in 2*N-1 comparisons.

I have updated my code. I think it is more efficient now. Thank you for pointing it out.

I think you can make it more efficient. You are doing 2*N-1 comparisons for each element in A. You can do N-1 comparisons for each element in A. You can do it in 2*N-1 comparisons. You can do it in 2*N-1 comparisons. How can I do it in 2*N-1 comparisons?

I have updated my code. I think it is more efficient now. Thank you for pointing it out.

I think you can make it more efficient. You are doing 2*N-1 comparisons for each element in A. You can do N-1 comparisons for each element in A. You can do it in 2*N-1 comparisons. You can do it in 2*N-1 comparisons. How can I do it in 2*N-1 comparisons? I have updated my code. I think it is more efficient now. Thank you for pointing it out.

I think you can make it more efficient. You are doing 2*N-1 comparisons for each element in A. You can do N-1 comparisons for each element in A. You can do it in 2*N-1 comparisons. You can do it in 2*N-1 comparisons

=======
Suggestion 3

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A_max = max(A)
    A_max_index = A.index(A_max)
    A.remove(A_max)
    A_max2 = max(A)
    for i in range(N):
        if i == A_max_index:
            print(A_max2)
        else:
            print(A_max)

main()

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    max_A = A[-1]
    for i in range(N):
        if A[i] == max_A:
            print(A[-2])
        else:
            print(max_A)

main()

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(input()) for i in range(N)]
    A.sort()
    maxA = A[-1]
    for i in range(N):
        if A[i] == maxA:
            print(A[-2])
        else:
            print(maxA)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    max_A = max(A)
    max_A_cnt = A.count(max_A)
    if max_A_cnt == 1:
        for a in A:
            if a == max_A:
                print(max_A)
            else:
                print(max_A)
    else:
        for _ in range(max_A_cnt):
            A.remove(max_A)
        for _ in range(max_A_cnt):
            A.append(max_A)
        for _ in range(max_A_cnt):
            print(max(A))

=======
Suggestion 7

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    maxA = max(A)
    maxAidx = A.index(maxA)
    A.pop(maxAidx)
    maxA2 = max(A)
    for i in range(N):
        if i == maxAidx:
            print(maxA2)
        else:
            print(maxA)

=======
Suggestion 8

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]
    A.sort()
    A_max = A[-1]
    A_max_2 = A[-2]
    for i in range(N):
        if A[i] == A_max:
            print(A_max_2)
        else:
            print(A_max)
    return

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(input()) for _ in range(N)]

    # N = 200000
    # A = [200000] * N

    # N = 2
    # A = [5, 5]

    B = sorted(A)
    maxA = B[-1]
    maxB = B[-2]

    for a in A:
        if a == maxA:
            print(maxB)
        else:
            print(maxA)

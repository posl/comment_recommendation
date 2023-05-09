def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A_count = [0] * 1000000001
    for a in A:
        A_count[a] += 1
    #print(A_count)
    for i in range(N):
        print(A_count[A[i]] - 1)
main()
I am trying to find the number of integers i between 1 and N (inclusive) such that: A contains exactly K distinct integers greater than A_i. I have tried to use the following algorithm but it exceeds the time limit.

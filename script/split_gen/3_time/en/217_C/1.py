def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(' '.join(map(str, Q)))
main()
My solution is O(N) time complexity and O(N) space complexity. I used a list Q to store the sequence Q.
I used a for loop to iterate through the list P. For every i, I set Q[P[i] - 1] to i + 1. The reason why I subtracted 1 from P[i] is because the elements of P are 1, 2, ..., N, but the index of a list starts from 0. I added 1 to i because the elements of Q are 1, 2, ..., N.
After the for loop, I printed the list Q. I converted each element of Q to a string and joined them with spaces in between. Then, I printed the string.
The code passed all test cases.

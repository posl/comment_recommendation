def is_permutation(N, A):
    if N != len(A):
        return False
    counter = 0
    for i in range(1, N + 1):
        if i in A:
            counter += 1
    return counter == N
N = int(input())
A = list(map(int, input().split()))

if __name__ == '__main__':
    is_permutation()
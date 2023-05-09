def is_multiple_of_k(A, B, K):
    for i in range(A, B+1):
        if i % K == 0:
            return True
    return False
K = int(input())
A, B = map(int, input().split())

if __name__ == '__main__':
    is_multiple_of_k()
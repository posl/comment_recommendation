def main():
    N, K = input().split()
    N = int(N)
    K = int(K)
    A = input().split()
    for k in range(K):
        A.pop(0)
        A.append('0')
    print(' '.join(A))

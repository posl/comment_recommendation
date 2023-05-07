def main():
    N, K = list(map(int, input().split()))
    for i in range(K):
        N = int(''.join(sorted(str(N), reverse=True))) - int(''.join(sorted(str(N))))
    print(N)

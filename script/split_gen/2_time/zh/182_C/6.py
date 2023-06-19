def main():
    N = int(input())
    K = len(str(N))
    if N % 3 == 0:
        print(0)
        return
    for i in range(K):
        for j in range(K):
            if i == j:
                continue
            if (N - int(str(N)[i]) - int(str(N)[j])) % 3 == 0:
                print(1)
                return
    for i in range(K):
        for j in range(K):
            for k in range(K):
                if i == j or j == k or k == i:
                    continue
                if (N - int(str(N)[i]) - int(str(N)[j]) - int(str(N)[k])) % 3 == 0:
                    print(2)
                    return
    print(-1)

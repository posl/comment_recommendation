def triangle(N, L):
    L.sort()
    count = 0
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                if L[i] + L[j] > L[k]:
                    count += 1
                else:
                    break
    return count
N = int(input())
L = list(map(int, input().split()))
print(triangle(N, L))

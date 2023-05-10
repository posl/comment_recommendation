def main():
    N, M = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split()))[1:])
    count = 0
    for i in range(1, M + 1):
        for j in range(N):
            if i in A[j]:
                if j == N - 1:
                    count += 1
                else:
                    continue
            else:
                break
    print(count)

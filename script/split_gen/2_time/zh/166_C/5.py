def main():
    N, K = map(int, input().split())
    A = []
    for i in range(K):
        d = int(input())
        A.append(list(map(int, input().split())))
    count = 0
    for i in range(N):
        for j in range(K):
            if i+1 not in A[j]:
                count += 1
                break
    print(count)

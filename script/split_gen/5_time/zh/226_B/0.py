def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(input().split())
    # print(L)
    L.sort()
    # print(L)
    cnt = 1
    for i in range(1, N):
        if L[i] != L[i-1]:
            cnt += 1
    print(cnt)

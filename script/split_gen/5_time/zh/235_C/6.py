def main():
    N, Q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        index = 0
        count = 0
        for j in range(N):
            if a[j] == x:
                count += 1
            if count == k:
                index = j + 1
                break
        if index == 0:
            print(-1)
        else:
            print(index)

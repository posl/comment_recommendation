def main():
    N, M = map(int, input().split())
    arr = [0 for i in range(N+1)]
    for i in range(M):
        l, r = map(int, input().split())
        arr[l-1] += 1
        arr[r] -= 1
    for i in range(1, N+1):
        arr[i] += arr[i-1]
    print(arr.count(M))

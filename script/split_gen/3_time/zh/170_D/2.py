def main():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 1
    for i in range(1, n):
        if arr[i] % arr[ans - 1] != 0:
            arr[ans] = arr[i]
            ans += 1
    print(ans)

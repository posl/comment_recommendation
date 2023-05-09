def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # print(n, k)
    # print(a)
    # print(b)
    a.sort()
    b.sort()
    # print(a)
    # print(b)
    # for i in range(n):
    #     if abs(a[i] - b[i]) > k:
    #         print("No")
    #         return
    # print("Yes")
    # print("Yes" if all(abs(a[i] - b[i]) <= k for i in range(n)) else "No")
    print("Yes" if all(abs(a[i] - b[i]) <= k for i in range(n)) else "No")

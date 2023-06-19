def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a_max = max(a)
    a_min = min(a)
    b_max = max(b)
    b_min = min(b)
    if a_max - a_min > k or b_max - b_min > k:
        print("No")
        return
    print("Yes")
    if a_max > b_max:
        for i in range(n):
            if a[i] > b[i]:
                print(b_max, end=" ")
            else:
                print(a[i], end=" ")
    else:
        for i in range(n):
            if a[i] < b[i]:
                print(a_max, end=" ")
            else:
                print(b[i], end=" ")

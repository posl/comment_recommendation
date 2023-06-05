def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        if p[i] == i + 1:
            count += 1
    if count == n:
        print("YES")
    elif count == n - 2:
        print("YES")
    else:
        print("NO")

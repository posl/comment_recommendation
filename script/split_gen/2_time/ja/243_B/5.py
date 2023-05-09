def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a2b = [0] * (n + 1)
    b2a = [0] * (n + 1)
    for i in range(n):
        a2b[a[i]] = i
        b2a[b[i]] = i
    ans1 = 0
    ans2 = 0
    for i in range(n):
        if a[i] == b[i]:
            ans1 += 1
        elif a2b[b[i]] == i:
            ans2 += 1
    print(ans1)
    print(ans2)

def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        temp = 0
        while p[i] != 1:
            p[i] = p[p[i] - 2]
            temp += 1
        ans = max(ans, temp)
    print(ans + 1)

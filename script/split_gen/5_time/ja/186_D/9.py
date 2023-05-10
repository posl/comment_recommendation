def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    ans = 0
    for i in range(n):
        ans += a_list[i] * (i + 1)
    ans -= sum(a_list)
    ans *= 2
    print(ans)

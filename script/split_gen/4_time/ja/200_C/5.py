def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod_200 = [0] * 200
    for a in A:
        mod_200[a % 200] += 1
    ans = 0
    for m in mod_200:
        ans += m * (m - 1) // 2
    print(ans)

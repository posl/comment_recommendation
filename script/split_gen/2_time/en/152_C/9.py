def main():
    N = int(input())
    P = [int(x) for x in input().split()]
    P = [p - 1 for p in P]
    ans = 0
    min = N
    for p in P:
        if p < min:
            ans += 1
            min = p
    print(ans)

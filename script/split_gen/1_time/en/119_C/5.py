def main():
    N, A, B, C = map(int, input().split())
    L = [int(input()) for _ in range(N)]
    ans = 10**9
    for i in range(4**N):
        a, b, c = 0, 0, 0
        cost = 0
        for j in range(N):
            if (i >> (2*j)) & 3 == 1:
                a += L[j]
                cost += 10
            elif (i >> (2*j)) & 3 == 2:
                b += L[j]
                cost += 10
            elif (i >> (2*j)) & 3 == 3:
                c += L[j]
                cost += 10
        if a and b and c:
            cost += abs(a-A) + abs(b-B) + abs(c-C) - 30
            ans = min(ans, cost)
    print(ans)

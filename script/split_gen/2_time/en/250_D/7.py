def main():
    N = int(input())
    ans = 0
    for p in range(2, 10**6):
        q = 1
        while p*q**3 <= N:
            q += 1
        ans += q-2
    print(ans)

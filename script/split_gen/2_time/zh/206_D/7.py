def main():
    N = int(input())
    A = list(map(int, input().split()))
    A_ = set(A)
    ans = 0
    for a in A_:
        if A.count(a) % 2 == 1:
            ans += 1
    print(ans)

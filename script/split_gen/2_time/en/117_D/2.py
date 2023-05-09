def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(40, -1, -1):
        zero = 0
        one = 0
        for a in A:
            if a >> i & 1:
                one += 1
            else:
                zero += 1
        if K >> i & 1:
            ans += (1 << i) * one
            A = [a for a in A if a >> i & 1]
        else:
            ans += (1 << i) * zero
            A = [a for a in A if not a >> i & 1]
    print(ans)

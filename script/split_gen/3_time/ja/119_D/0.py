def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.insert(0, -10**11)
    s.append(10**11)
    t.insert(0, -10**11)
    t.append(10**11)
    for i in range(Q):
        left = 0
        right = 0
        for j in range(A+1):
            if x[i] >= s[j]:
                left = s[j]
            else:
                break
        for j in range(B+1):
            if x[i] >= t[j]:
                right = t[j]
            else:
                break
        ans = min(abs(x[i]-left)+abs(left-right), abs(x[i]-right)+abs(left-right), abs(x[i]-left)+abs(left-right))
        print(ans)

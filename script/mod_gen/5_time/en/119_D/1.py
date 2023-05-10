def main():
    A, B, Q = map(int, input().split())
    S = [int(input()) for _ in range(A)]
    T = [int(input()) for _ in range(B)]
    X = [int(input()) for _ in range(Q)]
    for x in X:
        s1 = s2 = t1 = t2 = 0
        for i in range(A):
            if S[i] <= x:
                s1 = S[i]
            else:
                s2 = S[i]
                break
        for i in range(B):
            if T[i] <= x:
                t1 = T[i]
            else:
                t2 = T[i]
                break
        ans = []
        ans.append(max(x - s1, x - t1))
        ans.append(max(s2 - x, t2 - x))
        ans.append(2 * (x - s1) + (t2 - x))
        ans.append(2 * (t1 - x) + (x - s2))
        ans.append((s2 - x) + (x - t1))
        ans.append((t2 - x) + (x - s1))
        print(min(ans))

if __name__ == '__main__':
    main()
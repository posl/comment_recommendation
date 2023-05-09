def main():
    A, B, Q = map(int, input().split())
    s = [0]*A
    t = [0]*B
    x = [0]*Q
    for i in range(A):
        s[i] = int(input())
    for i in range(B):
        t[i] = int(input())
    for i in range(Q):
        x[i] = int(input())
    for i in range(Q):
        ans = 0
        for j in range(A):
            if x[i] < s[j]:
                if j == 0:
                    ans += s[j] - x[i]
                else:
                    if x[i] - s[j-1] < s[j] - x[i]:
                        ans += x[i] - s[j-1]
                    else:
                        ans += s[j] - x[i]
                break
            elif j == A-1:
                ans += x[i] - s[j]
        for j in range(B):
            if x[i] < t[j]:
                if j == 0:
                    ans += t[j] - x[i]
                else:
                    if x[i] - t[j-1] < t[j] - x[i]:
                        ans += x[i] - t[j-1]
                    else:
                        ans += t[j] - x[i]
                break
            elif j == B-1:
                ans += x[i] - t[j]
        print(ans)

if __name__ == '__main__':
    main()
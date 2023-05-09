def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A = [a for a in A if a < 0]
    A.sort(reverse=True)
    B = [a for a in A if a > 0]
    B.sort()
    C = [a for a in A if a == 0]
    D = [a for a in B if a == 0]
    if K <= len(A) * len(B):
        if len(C) > 0:
            print(0)
        else:
            if K <= len(A) * (len(B) - len(D)):
                l, r = 0, len(A) - 1
                while r - l > 1:
                    m = (l + r) // 2
                    if len(B) - len(D) - bisect.bisect_right(B, -A[m]) >= K:
                        r = m
                    else:
                        l = m
                if len(B) - len(D) - bisect.bisect_right(B, -A[l]) >= K:
                    print(A[l] * B[-1])
                else:
                    print(A[r] * B[-1])
            else:
                l, r = 0, len(B) - 1
                while r - l > 1:
                    m = (l + r) // 2
                    if len(A) - len(C) - bisect.bisect_left(A, -B[m]) >= K - (len(B) - len(D)) * (len(A) - len(C)):
                        r = m
                    else:
                        l = m
                if len(A) - len(C) - bisect.bisect_left(A, -B[l]) >= K - (len(B) - len(D)) * (len(A) - len(C)):
                    print(A[-1] * B[l])
                else:
                    print(A[-1] * B[r])
    else:
        if len(D) > 0:
            print(0)
        else:
            if K <= len(A) * len(B) + (len(A) * (len(A) - 1) // 2):
                l, r = 0, len(A) - 1
                while r - l > 1:
                    m =

if __name__ == '__main__':
    main()
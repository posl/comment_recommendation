def main():
    N, A, B = map(int, input().split())
    S = input()
    ans = 0
    for i in range(N):
        if S[i] == 'a':
            if A > 0:
                ans += 1
                A -= 1
        elif S[i] == 'b':
            if B > 0:
                ans += 1
                B -= 1
                if A > 0:
                    ans += 1
                    A -= 1
        else:
            if B > 0:
                ans += 1
                B -= 1
                if A > 0:
                    ans += 1
                    A -= 1
            elif A > 0:
                ans += 1
                A -= 1
    print(ans)

def main():
    N = int(input())
    ans = 0
    for A in range(1, N+1):
        for B in range(A, N+1):
            for C in range(B, N+1):
                if A*B*C <= N:
                    if A == B and B == C:
                        ans += 1
                    elif A == B or B == C:
                        ans += 3
                    else:
                        ans += 6
                else:
                    break
    print(ans)

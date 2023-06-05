def solve():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    #print(N, L, R)
    #print(A)
    if L >= 0:
        print(sum(A) + N * L)
    elif R <= 0:
        print(sum(A) + N * R)
    else:
        sumA = sum(A)
        minA = min(A)
        maxA = max(A)
        if sumA < 0:
            print(sumA + N * R)
        elif sumA > 0:
            print(sumA + N * L)
        else:
            if L < 0:
                print(sumA + N * (L - minA))
            else:
                print(sumA + N * (R - maxA))
solve()

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P_sorted = sorted(P)
    if P == P_sorted:
        print("YES")
    else:
        for i in range(N):
            for j in range(i+1, N):
                P_temp = P.copy()
                P_temp[i], P_temp[j] = P_temp[j], P_temp[i]
                if P_temp == P_sorted:
                    print("YES")
                    return
        print("NO")

if __name__ == '__main__':
    main()
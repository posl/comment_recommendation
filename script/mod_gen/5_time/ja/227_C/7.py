def main():
    N = int(input())
    ans = 0
    for A in range(1,N+1):
        for B in range(A,N+1):
            if A*B > N:
                break
            for C in range(B,N+1):
                if A*B*C > N:
                    break
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N, A, B = map(int, input().split())
    if A == 0:
        print(0)
        return
    if B == 0:
        print(N)
        return
    if A+B > N:
        print(0)
        return
    print(N//(A+B)*A + min(A,N%(A+B)))
main()

if __name__ == '__main__':
    main()
def main():
    N = input()
    N = list(N)
    N = [int(i) for i in N]
    N.sort()
    N.reverse()
    N1 = N[0]
    N2 = N[1]
    for i in range(2,len(N)):
        if N1 <= N2:
            N1 = N1*10 + N[i]
        else:
            N2 = N2*10 + N[i]
    print(N1*N2)
main()

if __name__ == '__main__':
    main()
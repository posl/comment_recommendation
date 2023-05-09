def main():
    N = input()
    N = list(N)
    N.sort(reverse=True)
    N = ''.join(N)
    N = int(N)
    N = str(N)
    N = list(N)
    N = [int(x) for x in N]
    a = N[0]
    for i in range(1,len(N)):
        a = a*10 + N[i]
    b = N[0]
    for i in range(1,len(N)):
        b = b + N[i]*10**(i)
    print(a*b)

if __name__ == '__main__':
    main()
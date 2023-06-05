def main():
    N = input()
    N1 = list(N)
    N2 = N1.copy()
    N1.sort(reverse=True)
    N2.sort()
    if N2[0] == '0':
        N2.pop(0)
        N2.append('0')
    N1 = int(''.join(N1))
    N2 = int(''.join(N2))
    print(N1*N2)

if __name__ == '__main__':
    main()
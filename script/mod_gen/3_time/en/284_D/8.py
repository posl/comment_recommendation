def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        p = 1
        q = 1
        for j in range(2, int(N**(1/3))+1):
            if N%j == 0:
                p = j
                q = N//j
                break
        print(p, q)

if __name__ == '__main__':
    main()
def main():
    N = int(input())
    if N == 1:
        print(0)
        return
    # M_1 + M_2 + ... + M_N = (N-1) + (N-2) + ... + 1 = N*(N-1)/2
    print(N*(N-1)//2)

if __name__ == '__main__':
    main()
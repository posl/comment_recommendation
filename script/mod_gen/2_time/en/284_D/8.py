def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        for i in range(2, int(N**0.5)+1):
            if N%i==0:
                print(i, N//i)
                break

if __name__ == '__main__':
    main()
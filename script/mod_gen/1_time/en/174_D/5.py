def main():
    N = int(input())
    S = input()
    R = S.count('R')
    W = N - R
    print(min(R, W))

if __name__ == '__main__':
    main()
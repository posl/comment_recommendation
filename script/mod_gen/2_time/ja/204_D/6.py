def main():
    N = int(input())
    T = list(map(int,input().split()))
    T.sort(reverse=True)
    if N == 1:
        print(T[0])
    else:
        print(T[0]+T[1])

if __name__ == '__main__':
    main()
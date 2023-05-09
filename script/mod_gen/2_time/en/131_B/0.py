def main():
    N, L = map(int, input().split())
    if L >= 0:
        print(sum(range(L, L+N-1)))
    elif L+N-1 <= 0:
        print(sum(range(L+1, L+N)))
    else:
        print(sum(range(L, L+N-1))-L)
main()

if __name__ == '__main__':
    main()
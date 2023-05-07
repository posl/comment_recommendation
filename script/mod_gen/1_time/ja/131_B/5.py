def main():
    N, L = map(int, input().split())
    if L >= 0:
        print(sum(list(range(L+1, L+N))))
    elif L+N <= 0:
        print(sum(list(range(L+N, L))))
    else:
        print(sum(list(range(L, L+N))))

if __name__ == '__main__':
    main()
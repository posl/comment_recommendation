def main():
    N, L = map(int, input().split())
    apple = [L+i-1 for i in range(1, N+1)]
    if L <= 0 <= L+N-1:
        print(sum(apple)-0)
    elif L+N-1 < 0:
        print(sum(apple)-apple[-1])
    else:
        print(sum(apple)-apple[0])

if __name__ == '__main__':
    main()
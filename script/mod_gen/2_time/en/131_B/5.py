def main():
    N, L = map(int, input().split())
    apple = [L+i-1 for i in range(1, N+1)]
    if apple[0] >= 0:
        print(sum(apple[1:]))
    elif apple[-1] <= 0:
        print(sum(apple[:-1]))
    else:
        print(sum(apple[:apple.index(0)])+sum(apple[apple.index(0)+1:]))

if __name__ == '__main__':
    main()
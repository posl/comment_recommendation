def main():
    H,W = map(int,input().strip().split())
    S = [input() for _ in range(H)]
    print(sum([s.count('#') for s in S]))

if __name__ == '__main__':
    main()
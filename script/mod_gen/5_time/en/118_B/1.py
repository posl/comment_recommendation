def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(N)]
    print(len(set.intersection(*map(set, A))))

if __name__ == '__main__':
    main()
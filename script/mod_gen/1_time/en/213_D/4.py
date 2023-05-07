def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N-1)]
    AB.sort(key=lambda x: x[1])
    AB.sort(key=lambda x: x[0])
    print(' '.join(str(x) for x in [1] + [AB[i][1] for i in range(N-1)] + [1]))

if __name__ == '__main__':
    main()
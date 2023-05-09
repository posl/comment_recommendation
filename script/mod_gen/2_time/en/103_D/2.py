def main():
    N, M = map(int, input().split())
    bridges = [0] * N
    for i in range(M):
        a, b = map(int, input().split())
        bridges[a-1] += 1
        bridges[b-1] += 1
    print(bridges.count(1))

if __name__ == '__main__':
    main()
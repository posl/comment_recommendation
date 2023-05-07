def main():
    N, M = map(int, input().split())
    sc = [list(map(int, input().split())) for _ in range(M)]
    for i in range(1000):
        if len(str(i)) == N:
            for j in sc:
                if str(i)[j[0]-1] != str(j[1]):
                    break
            else:
                print(i)
                return
    print(-1)

if __name__ == '__main__':
    main()
def main():
    N, M = map(int, input().split())
    a_b = [list(map(int, input().split())) for _ in range(M)]
    a_b.sort(key=lambda x: x[1])
    count = 0
    bridge = [False] * N
    for i in range(M):
        if bridge[a_b[i][0]-1] == False and bridge[a_b[i][1]-1] == False:
            bridge[a_b[i][1]-1] = True
            count += 1
    print(count)

if __name__ == '__main__':
    main()
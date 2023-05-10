def main():
    N, S, D = map(int, input().split())
    spell = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        if spell[i][0] < S and spell[i][1] > D:
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()
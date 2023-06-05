def main():
    n, k = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(n)]
    scores.sort(key=lambda x: x[0] + x[1] + x[2], reverse=True)
    print(scores)
    for i in range(n):
        if scores[i][0] + scores[i][1] + scores[i][2] > scores[k - 1][0] + scores[k - 1][1] + scores[k - 1][2]:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()
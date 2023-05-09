def main():
    n = int(input())
    a = [input().split() for i in range(n)]
    score = {}
    for i in range(n):
        if a[i][0] not in score:
            score[a[i][0]] = int(a[i][1])
        else:
            score[a[i][0]] = max(score[a[i][0]], int(a[i][1]))
    for i in range(n):
        if score[a[i][0]] == int(a[i][1]):
            print(i+1)
            exit()
main()

if __name__ == '__main__':
    main()
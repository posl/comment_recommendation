def main():
    n, k = map(int, input().split())
    score = []
    for _ in range(n):
        score.append(sum(map(int, input().split())))
    score.sort(reverse = True)
    for i in range(n):
        if score[i] < score[k - 1]:
            print("No")
        else:
            print("Yes")

if __name__ == '__main__':
    main()
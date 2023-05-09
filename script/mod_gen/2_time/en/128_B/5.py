def main():
    N = int(input())
    city = [0]*N
    score = [0]*N
    for i in range(N):
        city[i], score[i] = input().split()
        score[i] = int(score[i])
    for i in range(N):
        print(score.index(max(score))+1)
        score[score.index(max(score))] = -1

if __name__ == '__main__':
    main()
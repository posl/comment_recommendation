def main():
    N = int(input())
    city_score = []
    for i in range(N):
        city_score.append(input().split() + [i+1])
    city_score.sort()
    city_score.sort(key=lambda x: x[1], reverse=True)
    for i in range(N):
        print(city_score[i][2])

if __name__ == '__main__':
    main()
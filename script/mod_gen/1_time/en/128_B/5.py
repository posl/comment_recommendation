def main():
    n = int(input())
    city_score = []
    for i in range(n):
        city, score = input().split()
        city_score.append((city, int(score), i+1))
    city_score.sort(key=lambda x: (x[0], -x[1]))
    for _, _, i in city_score:
        print(i)

if __name__ == '__main__':
    main()
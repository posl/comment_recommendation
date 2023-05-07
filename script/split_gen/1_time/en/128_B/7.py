def main():
    N = int(input())
    city_score = []
    for i in range(N):
        city, score = input().split()
        city_score.append((city, int(score), i+1))
    city_score.sort(key=lambda x: (x[0], -x[1]))
    for x in city_score:
        print(x[2])
main()

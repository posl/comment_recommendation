def get_city_and_score():
    city_and_score = {}
    num = int(input())
    for i in range(num):
        city, score = input().split()
        city_and_score[city] = int(score)
    return city_and_score

if __name__ == '__main__':
    get_city_and_score()
def main():
    n = int(input())
    #city = []
    #score = []
    #for i in range(n):
    #    c,s = input().split()
    #    city.append(c)
    #    score.append(s)
    #city_score = zip(city,score)
    #city_score = sorted(city_score, key=lambda x: x[0])
    #city_score = sorted(city_score, key=lambda x: x[1], reverse=True)
    #for i in range(n):
    #    print(city_score[i][0])
    city_score = []
    for i in range(n):
        c,s = input().split()
        city_score.append((c,s))
    city_score.sort(key=lambda x: x[0])
    city_score.sort(key=lambda x: x[1], reverse=True)
    for i in range(n):
        print(city_score[i][0])

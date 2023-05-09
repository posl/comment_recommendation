Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    cities = []
    for i in range(m):
        p, y = map(int, input().split())
        cities.append([p, y, i])
    cities.sort(key=lambda x: (x[0], x[1]))
    prefecture = cities[0][0]
    count = 0
    for i in range(m):
        if prefecture == cities[i][0]:
            count += 1
        else:
            prefecture = cities[i][0]
            count = 1
        cities[i].append(count)
    cities.sort(key=lambda x: x[2])
    for i in range(m):
        print('{:06d}{:06d}'.format(cities[i][0], cities[i][3]))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(M):
        P, Y = map(int, input().split())
        cities.append([P, Y, i])
    cities.sort(key=lambda x: (x[0], x[1]))
    pref = cities[0][0]
    cnt = 1
    for i in range(M):
        if pref == cities[i][0]:
            cities[i].append(cnt)
            cnt += 1
        else:
            pref = cities[i][0]
            cnt = 1
            cities[i].append(cnt)
            cnt += 1
    cities.sort(key=lambda x: x[2])
    for i in range(M):
        print('{:06}{:06}'.format(cities[i][0], cities[i][3]))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    d = {}
    for i in range(m):
        p, y = map(int, input().split())
        if p in d:
            d[p].append([y, i])
        else:
            d[p] = [[y, i]]
    for k in d.keys():
        d[k].sort()
    ans = []
    for k in d.keys():
        for i in range(len(d[k])):
            ans.append([d[k][i][1], str(k).zfill(6) + str(i+1).zfill(6)])
    ans.sort()
    for i in range(len(ans)):
        print(ans[i][1])

=======
Suggestion 4

def main():
    n, m = map(int, input().split())
    city = []
    for i in range(m):
        p, y = map(int, input().split())
        city.append([i, p, y])
    city.sort(key=lambda x: x[2])
    city.sort(key=lambda x: x[1])
    #print(city)
    for i in range(m):
        city[i].append(str(city[i][1]).zfill(6) + str(i+1).zfill(6))
    city.sort(key=lambda x: x[0])
    for i in range(m):
        print(city[i][3])

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: (x[0], x[1]))

    prefectures = [0] * (n + 1)
    for p, y in p_y:
        prefectures[p] += 1

    city_numbers = [0] * (n + 1)
    for i in range(1, n + 1):
        city_numbers[i] = city_numbers[i - 1] + prefectures[i]

    for p, y in p_y:
        print('{0:06}{1:06}'.format(p, city_numbers[p]))
        city_numbers[p] += 1

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    cities = []
    for i in range(M):
        cities.append(list(map(int, input().split())) + [i])
    cities.sort(key=lambda x: x[1])
    prefecture = 0
    counter = 1
    for i in range(M):
        if prefecture != cities[i][0]:
            counter = 1
            prefecture = cities[i][0]
        cities[i][0] = str(cities[i][0])
        cities[i][1] = str(counter).zfill(6)
        cities[i][2] = str(cities[i][2]).zfill(6)
        counter += 1
    cities.sort(key=lambda x: x[3])
    for i in range(M):
        print(cities[i][0] + cities[i][1] + cities[i][2])

=======
Suggestion 7

def main():
    n, m = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(m)]
    cities = sorted(cities, key=lambda x: x[1])
    ans = []
    for i, city in enumerate(cities):
        ans.append([city[0], str(i+1).zfill(6)])
    ans = sorted(ans, key=lambda x: x[0])
    for a in ans:
        print(str(a[0]).zfill(6)+a[1])

=======
Suggestion 8

def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x: x[1])
    p_y2 = [[p_y[i][0], p_y[i][1], i+1] for i in range(m)]
    p_y2.sort(key=lambda x: x[0])
    p_y2 = [[p_y2[i][0], p_y2[i][1], p_y2[i][2], str(p_y2[i][0]).zfill(6), str(p_y2[i][2]).zfill(6)] for i in range(m)]
    for i in range(m):
        print(p_y2[i][3]+p_y2[i][4])

=======
Suggestion 9

def solution():
    # This is the main function
    # Write your code here
    n, m = map(int, input().split())
    p_y = []
    for i in range(m):
        p, y = map(int, input().split())
        p_y.append((p, y, i))
    p_y.sort(key=lambda x: x[1])
    cities = [0] * (n + 1)
    for p, y, i in p_y:
        cities[p] += 1
        print(f"{p:06}{cities[p]:06}")

=======
Suggestion 10

def main():
    pass

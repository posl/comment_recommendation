Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    P = []
    for i in range(N):
        s, p = input().split()
        S.append(s)
        P.append(int(p))
    for i in range(N):
        for j in range(N - 1, i, -1):
            if S[j] < S[j - 1]:
                S[j], S[j - 1] = S[j - 1], S[j]
                P[j], P[j - 1] = P[j - 1], P[j]
            elif S[j] == S[j - 1]:
                if P[j] > P[j - 1]:
                    S[j], S[j - 1] = S[j - 1], S[j]
                    P[j], P[j - 1] = P[j - 1], P[j]
    for i in range(N):
        print(i + 1)

=======
Suggestion 2

def main():
    n = int(input())
    l = []
    for i in range(n):
        s, p = input().split()
        l.append((s, -int(p), i+1))
    l.sort()
    for i in l:
        print(i[2])

=======
Suggestion 3

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, int(p), i + 1))
    restaurants.sort(key=lambda x: (x[0], -x[1]))
    for restaurant in restaurants:
        print(restaurant[2])

=======
Suggestion 4

def main():
    n = int(input())
    restaurants = []
    for i in range(n):
        s, p = input().split()
        restaurants.append((s, -int(p), i + 1))
    restaurants.sort()
    for s, p, i in restaurants:
        print(i)

=======
Suggestion 5

def main():
    n = int(input())
    r = []
    for i in range(n):
        s, p = input().split()
        r.append((s, -int(p), i+1))
    r.sort()
    for _, _, i in r:
        print(i)

=======
Suggestion 6

def main():
    n = int(input())
    city_score = []
    for i in range(n):
        city, score = input().split()
        city_score.append((city, int(score), i+1))
    city_score.sort(key=lambda x: (x[0], -x[1]))
    for _, _, i in city_score:
        print(i)

=======
Suggestion 7

def main():
    N = int(input())
    restaurants = [input().split() for _ in range(N)]
    restaurants.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(N):
        print(restaurants[i][2])

=======
Suggestion 8

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

=======
Suggestion 9

def main():
    N = int(input())
    city_score = []
    for i in range(N):
        city_score.append(input().split() + [i+1])
    city_score.sort()
    city_score.sort(key=lambda x: x[1], reverse=True)
    for i in range(N):
        print(city_score[i][2])

=======
Suggestion 10

def main():
    N = int(input())
    #print(N)
    #print(type(N))
    #S = []
    #P = []
    #for i in range(N):
    #    (S_i, P_i) = input().split()
    #    S.append(S_i)
    #    P.append(int(P_i))
    #print(S)
    #print(P)
    #print(type(S))
    #print(type(P))
    #print(type(S[0]))
    #print(type(P[0]))
    #print(type(S[0][0]))
    #print(type(P[0][0]))
    #print(type(P[0][1]))
    #print(type(P[0][2]))
    #print(type(P[0][3]))
    #print(type(P[0][4]))
    #print(type(P[0][5]))
    #print(type(P[0][6]))
    #print(type(P[0][7]))
    #print(type(P[0][8]))
    #print(type(P[0][9]))
    #print(type(P[0][10]))
    #print(type(P[0][11]))
    #print(type(P[0][12]))
    #print(type(P[0][13]))
    #print(type(P[0][14]))
    #print(type(P[0][15]))
    #print(type(P[0][16]))
    #print(type(P[0][17]))
    #print(type(P[0][18]))
    #print(type(P[0][19]))
    #print(type(P[0][20]))
    #print(type(P[0][21]))
    #print(type(P[0][22]))
    #print(type(P[0][23]))
    #print(type(P[0][24]))
    #print(type(P[0][25]))
    #print(type(P[0][26]))
    #print(type(P[0][27]))
    #print(type(P[0][28]))
    #print(type(P[0][29]))
    #print(type(P[0][30]))
    #print(type(P[0][31]))
    #print(type(P[0][32]))
    #print(type(P[0][33]))
    #print(type(P[0][34]))
    #print(type(P[0][35]))
    #print(type(P[0][36]))
    #print(type(P[0][37]))
    #print

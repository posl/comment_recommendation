def main():
    n = int(input())
    ab = []
    for i in range(n-1):
        ab.append(list(map(int, input().split())))
    #print(ab)
    #print(ab[0][0])
    #print(ab[0][1])
    #print(ab[1][0])
    #print(ab[1][1])
    city = [0] * (n+1)
    #print(city)
    city[1] = 1
    #print(city)
    for i in range(n-1):
        #print("i = {}".format(i))
        #print(ab[i][0])
        #print(ab[i][1])
        if city[ab[i][0]] == 1:
            city[ab[i][1]] = 1
            print(ab[i][0], end=' ')
        elif city[ab[i][1]] == 1:
            city[ab[i][0]] = 1
            print(ab[i][1], end=' ')
        else:
            print("error")
            exit()
    print(1)

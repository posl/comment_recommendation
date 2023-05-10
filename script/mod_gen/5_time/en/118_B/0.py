def main():
    n, m = map(int, input().split())
    k = []
    a = []
    for i in range(n):
        ki, ai = map(int, input().split())
        k.append(ki)
        a.append(ai)
    #print(n, m)
    #print(k)
    #print(a)
    food = [0] * m
    for i in range(n):
        for j in range(k[i]):
            food[a[i][j] - 1] += 1
    #print(food)
    print(food.count(n))

if __name__ == '__main__':
    main()
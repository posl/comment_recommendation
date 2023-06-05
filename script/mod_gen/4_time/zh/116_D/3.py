def main():
    n, k = map(int, input().split())
    sushi = []
    for _ in range(n):
        sushi.append(list(map(int, input().split())))
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    sushi.sort(key=lambda x: x[1], reverse=True)
    sushi.sort(key=lambda x: x[0])
    print(sushi)
    print(sushi[0:k])
    # for i in range(k):
    #     print(sushi[i][1])

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    ab = []
    for i in range(n):
        ab.append(list(map(int, input().split())))
    ab.sort(key=lambda x: x[0])
    maxt = 0
    for i in range(n):
        maxt = max(maxt, ab[i][0]/ab[i][1])
    print(sum(map(lambda x: x[0], ab)) - maxt/2)

if __name__ == '__main__':
    main()
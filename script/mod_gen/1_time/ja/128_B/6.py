def main():
    N = int(input())
    city = []
    for i in range(N):
        city.append(input().split())
    city.sort(key=lambda x: (x[0], -int(x[1])))
    for i in range(N):
        print(city.index(city[i])+1)

if __name__ == '__main__':
    main()
def main():
    N = int(input())
    city = []
    for i in range(N):
        S, P = input().split()
        city.append([S, int(P), i+1])
    city.sort(key=lambda x: (x[0], -x[1]))
    for i in city:
        print(i[2])

if __name__ == '__main__':
    main()
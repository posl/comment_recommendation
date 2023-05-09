def main():
    N = int(input())
    data = []
    for i in range(N):
        S, P = input().split()
        data.append([S, int(P), i+1])
    data.sort(key=lambda x: (-x[1], x[0]))
    for i in data:
        print(i[2])

if __name__ == '__main__':
    main()
def main():
    N = int(input())
    data = []
    for i in range(N):
        s, p = input().split()
        data.append([s, int(p), i + 1])
    data.sort(key=lambda x: (x[0], -x[1]))
    for i in data:
        print(i[2])

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    data = []
    for i in range(n):
        s, p = input().split()
        data.append([s, -int(p), i+1])
    data.sort()
    for d in data:
        print(d[2])

if __name__ == '__main__':
    main()
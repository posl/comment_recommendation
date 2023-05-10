def main():
    n = int(input())
    ladders = []
    for i in range(n):
        a, b = map(int, input().split())
        ladders.append((a, b))
    ladders.sort(key=lambda x: x[0])
    print(ladders[-1][0] + ladders[-1][1])

if __name__ == '__main__':
    main()
def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(tuple(map(int, input().split())))
    ladders.sort(key=lambda x: x[0])
    print(ladders[-1][1])
main()

if __name__ == '__main__':
    main()
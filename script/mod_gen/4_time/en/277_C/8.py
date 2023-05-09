def main():
    N = int(input())
    ladders = []
    for i in range(N):
        ladders.append(tuple(map(int, input().split())))
    A = sorted(ladders, key=lambda x: x[0])
    B = sorted(ladders, key=lambda x: x[1])
    print(max(A[-1][0], B[-1][1]))

if __name__ == '__main__':
    main()
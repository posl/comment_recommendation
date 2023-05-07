def main():
    N = int(input())
    array = []
    for i in range(N):
        array.append(list(map(int, input().split())))
    ball = []
    for i in range(N):
        if array[i][0] == 1:
            for j in range(array[i][2]):
                ball.append(array[i][1])
        else:
            print(sum(ball[:array[i][1]]))
            del ball[:array[i][1]]
main()

if __name__ == '__main__':
    main()
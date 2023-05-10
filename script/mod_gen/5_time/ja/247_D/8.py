def main():
    q = int(input())
    ball = []
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            ball.append(int(query[1]))
        else:
            cnt = int(query[1])
            sum = 0
            for j in range(cnt):
                sum += ball.pop(0)
            print(sum)

if __name__ == '__main__':
    main()
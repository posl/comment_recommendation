def main():
    Q = int(input())
    queue = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            queue.append([int(query[1]), int(query[2])])
        else:
            c = int(query[1])
            sum = 0
            for j in range(c):
                sum += queue[j][0]
            print(sum)
            queue = queue[c:]

if __name__ == '__main__':
    main()
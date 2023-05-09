def main():
    Q = int(input())
    queue = []
    for i in range(Q):
        query = input().split()
        if query[0] == "1":
            queue.append(int(query[1]))
            queue = queue + [int(query[1])] * int(query[2])
        else:
            print(sum(queue[:int(query[1])]))
            queue = queue[int(query[1]):]

if __name__ == '__main__':
    main()
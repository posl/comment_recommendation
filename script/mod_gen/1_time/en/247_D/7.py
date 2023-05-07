def main():
    q = int(input())
    queue = []
    for i in range(q):
        queue.append(input().split())
    for i in range(q):
        if queue[i][0] == '1':
            for j in range(int(queue[i][2])):
                queue.append([queue[i][1]])
        else:
            sum = 0
            for j in range(int(queue[i][1])):
                sum += int(queue[j][0])
            print(sum)
            for j in range(int(queue[i][1])):
                del queue[0]
main()

if __name__ == '__main__':
    main()
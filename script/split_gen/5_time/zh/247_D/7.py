def main():
    q = int(input())
    queue = []
    for i in range(q):
        query = input().split()
        if query[0] == "1":
            queue.append(query[1])
        elif query[0] == "2":
            sum = 0
            for j in range(int(query[1])):
                sum += int(queue.pop(0))
            print(sum)
main()

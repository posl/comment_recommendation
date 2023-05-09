def main():
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int, input().split())))
    # print(query)
    stack = []
    for i in range(Q):
        if query[i][0] == 1:
            for j in range(query[i][2]):
                stack.append(query[i][1])
        elif query[i][0] == 2:
            sum = 0
            for j in range(query[i][1]):
                sum += stack.pop(0)
            print(sum)

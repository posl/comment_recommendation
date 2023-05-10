def main():
    q = int(input())
    #print(q)
    stack = []
    for i in range(q):
        #print(i)
        query = input().split()
        #print(query)
        if query[0] == "1":
            stack.append(int(query[1]))
        else:
            c = int(query[1])
            sum = 0
            for j in range(c):
                sum += stack.pop()
            print(sum)

if __name__ == '__main__':
    main()
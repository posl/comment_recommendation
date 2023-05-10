def main():
    #n = int(input())
    #a, b = list(map(int, input().split()))
    #s = input()
    #s = input().split()
    q = int(input())
    #query = [list(map(int, input().split())) for i in range(q)]
    query = [input().split() for i in range(q)]
    #print(query)
    #print(query[0][0])
    s = []
    for i in range(q):
        if query[i][0] == "1":
            s.append(int(query[i][1]))
        elif query[i][0] == "2":
            num = int(query[i][1])
            count = int(query[i][2])
            for j in range(count):
                if num in s:
                    s.remove(num)
                else:
                    break
        else:
            s.sort()
            print(s[-1] - s[0])
    #print(s)

if __name__ == '__main__':
    main()
def main():
    n, m = map(int, input().split())
    edge = []
    for i in range(m):
        edge.append(list(map(int, input().split())))
    edge.sort(key=lambda x: x[0])
    count = 0
    for i in range(n-1):
        for j in range(i+1, n):
            flag = 0
            for e in edge:
                if e[0] == i+1 and e[1] == j+1:
                    flag = 1
                    break
            if flag == 0:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
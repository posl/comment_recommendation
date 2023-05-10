def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int,input().split())))
    for i in range(n):
        if l[i][0] == 1:
            l.append([l[i][1],l[i][2]])
        else:
            print(sum([l[j][0] for j in range(len(l)) if j < l[i][1]]))

if __name__ == '__main__':
    main()
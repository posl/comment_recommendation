def main():
    n = int(input())
    dic = {}
    for _ in range(n):
        line = input().split()
        line = [int(i) for i in line]
        if line[0] not in dic:
            dic[line[0]] = set()
        dic[line[0]].add(tuple(line[1:]))
    print(len(dic))

if __name__ == '__main__':
    main()
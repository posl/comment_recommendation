def main():
    N = int(input())
    S = [input() for i in range(N)]
    dic = {}
    for s in S:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    max = 0
    for k, v in dic.items():
        if v > max:
            max = v
    for k, v in sorted(dic.items()):
        if v == max:
            print(k)

if __name__ == '__main__':
    main()
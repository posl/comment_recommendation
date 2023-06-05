def main():
    n = int(input())
    s = [input() for i in range(n)]
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_num = max(dic.values())
    ans = []
    for k,v in dic.items():
        if v == max_num:
            ans.append(k)
    ans.sort()
    for i in ans:
        print(i)

if __name__ == '__main__':
    main()
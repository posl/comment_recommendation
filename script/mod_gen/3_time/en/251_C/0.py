def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s, t = input().split()
        t = int(t)
        if s not in dic:
            dic[s] = t
        else:
            dic[s] = max(dic[s], t)
    print(n - len(dic))

if __name__ == '__main__':
    main()
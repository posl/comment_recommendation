def main():
    n = int(input())
    dic = {}
    for i in range(n):
        s = input()
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    max = 0
    for key in dic:
        if dic[key] > max:
            max = dic[key]
    for key in sorted(dic):
        if dic[key] == max:
            print(key)

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    max = 0
    max_name = ''
    dic = {}
    for i in range(n):
        name = input()
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
        if dic[name] > max:
            max = dic[name]
            max_name = name
    print(max_name)

if __name__ == '__main__':
    main()
def main():
    num = int(input())
    dic = {}
    for i in range(num):
        name = input()
        if name in dic:
            dic[name] += 1
        else:
            dic[name] = 1
    max = 0
    for i in dic:
        if dic[i] > max:
            max = dic[i]
            max_name = i
    print(max_name)

if __name__ == '__main__':
    main()
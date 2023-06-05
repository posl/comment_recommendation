def main():
    n = int(input())
    list1 = []
    for i in range(n):
        s, p = input().split()
        list1.append((s, int(p)))
    list1.sort(key=lambda x: x[1], reverse=True)
    list1.sort(key=lambda x: x[0])
    for i in list1:
        print(list1.index(i) + 1)

if __name__ == '__main__':
    main()
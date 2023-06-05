def main():
    x = input()
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort(key=lambda i: [x.index(j) for j in i])
    for i in s:
        print(i)

if __name__ == '__main__':
    main()
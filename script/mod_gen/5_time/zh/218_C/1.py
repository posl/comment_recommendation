def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        t.append(input())
    # print(s)
    # print(t)
    s = rotate(s)
    # print(s)
    if s == t:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
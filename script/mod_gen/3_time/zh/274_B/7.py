def main():
    h,w = map(int,input().split())
    lst = []
    for i in range(h):
        lst.append(input())
    for i in range(w):
        count = 0
        for j in range(h):
            if lst[j][i] == '#':
                count += 1
        print(count,end=' ')
    print()

if __name__ == '__main__':
    main()
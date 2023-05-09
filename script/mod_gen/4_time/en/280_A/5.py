def main():
    h,w = map(int,input().split())
    s = [input() for i in range(h)]
    count = 0
    for i in range(h):
        count += s[i].count('#')
    print(count)

if __name__ == '__main__':
    main()
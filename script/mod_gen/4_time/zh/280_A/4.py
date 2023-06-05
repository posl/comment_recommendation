def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    print(sum(s[i][j] == '#' for i in range(h) for j in range(w)))
    #print(sum(s[i][j] == '#' for i in range(h) for j in range(w)))  # 用for循环的话，会超时
    #print(sum(s[i].count('#') for i in range(h)))  # 用for循环的话，会超时

if __name__ == '__main__':
    main()
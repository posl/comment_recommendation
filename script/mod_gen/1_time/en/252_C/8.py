def main():
    n = int(input())
    s = [input() for i in range(n)]
    print(sum([min([abs(int(s[i][j]) - int(s[i][j+1])) for j in range(9)]) for i in range(n)]))

if __name__ == '__main__':
    main()
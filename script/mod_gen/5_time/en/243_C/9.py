def main():
    n = int(input())
    xy = [list(map(int, input().split())) for _ in range(n)]
    s = input()
    #print(xy)
    #print(s)
    def check(xy, s):
        for i in range(len(s) - 1):
            if s[i] == 'R':
                for j in range(i + 1, len(s)):
                    if s[j] == 'L':
                        if xy[i][0] < xy[j][0] and xy[i][1] == xy[j][1]:
                            return True
        return False
    if check(xy, s):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
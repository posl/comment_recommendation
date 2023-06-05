def main():
    l, q = map(int, input().split())
    mark = [0 for i in range(l+1)]
    mark[0] = 1
    mark[l] = 1
    for i in range(q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        else:
            left = x
            while mark[left] == 0:
                left -= 1
            right = x
            while mark[right] == 0:
                right += 1
            print(right - left)

if __name__ == '__main__':
    main()
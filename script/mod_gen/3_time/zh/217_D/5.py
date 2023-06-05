def main():
    L, Q = map(int, input().split())
    mark = [0] * (L+1)
    mark[0] = 1
    mark[L] = 1
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        else:
            left = 0
            right = L
            while left <= right:
                mid = (left + right) // 2
                if mark[mid] == 1:
                    right = mid - 1
                else:
                    left = mid + 1
            left = left - 1
            left2 = 0
            right2 = L
            while left2 <= right2:
                mid2 = (left2 + right2) // 2
                if mark[mid2] == 1:
                    left2 = mid2 + 1
                else:
                    right2 = mid2 - 1
            right2 = right2 + 1
            print(right2 - left)

if __name__ == '__main__':
    main()
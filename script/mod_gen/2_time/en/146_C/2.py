def main():
    A, B, X = map(int, input().split())
    #print(A, B, X)
    left = 0
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        if A * mid + B * len(str(mid)) <= X:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()
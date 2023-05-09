def main():
    K = int(input())
    K -= 1
    a = K // 3
    b = K % 3
    ans = 2 ** a
    if b == 0:
        ans *= 2
    elif b == 1:
        ans *= 20
    elif b == 2:
        ans *= 22
    print(ans)

if __name__ == '__main__':
    main()
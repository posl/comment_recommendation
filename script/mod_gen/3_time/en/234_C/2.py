def main():
    K = int(input())
    ans = ""
    while K > 0:
        K -= 1
        ans = str(K % 3) + ans
        K //= 3
    print(ans)

if __name__ == '__main__':
    main()
def main():
    K = int(input())
    ans = ""
    while K > 0:
        ans = str(K % 3) + ans
        K //= 3
    ans = ans.replace("1", "2")
    ans = ans.replace("0", "1")
    print(ans)

if __name__ == '__main__':
    main()
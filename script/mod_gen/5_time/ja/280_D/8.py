def main():
    k = int(input())
    if k % 2 == 0 or k % 5 == 0:
        print(-1)
        return
    else:
        if k == 1:
            print(1)
            return
        else:
            ans = 1
            for i in range(1, k+1):
                ans *= i
                ans = ans % k
                if ans == 0:
                    print(i)
                    return

if __name__ == '__main__':
    main()
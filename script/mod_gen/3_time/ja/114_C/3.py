def main():
    N = int(input())
    ans = 0
    for i in range(3, 10):
        for j in range(3, 10):
            for k in range(3, 10):
                if i == 7 or i == 5 or i == 3:
                    if j == 7 or j == 5 or j == 3:
                        if k == 7 or k == 5 or k == 3:
                            num = 100 * i + 10 * j + k
                            if num <= N:
                                ans += 1
    print(ans)

if __name__ == '__main__':
    main()
def main():
    N = int(input())
    ans = 0
    for i in range(3, 10):
        for j in range(3, 10):
            for k in range(3, 10):
                num = i * 100 + j * 10 + k
                if num > N:
                    continue
                if i == 7 or j == 7 or k == 7:
                    if i == 5 or j == 5 or k == 5:
                        if i == 3 or j == 3 or k == 3:
                            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()
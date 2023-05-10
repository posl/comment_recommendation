def main():
    K = int(input())
    ans = 0
    for i in range(1, K + 1):
        if (K % i == 0):
            ans = i
    print(ans)
    return

if __name__ == '__main__':
    main()
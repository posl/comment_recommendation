def main():
    N = int(input())
    ans = 0
    for p in range(2, 40):
        for e in range(1, 40):
            if N % (p**e) == 0:
                ans = e
    print(ans)

if __name__ == '__main__':
    main()
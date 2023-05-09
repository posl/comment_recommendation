def main():
    a, b, t = map(int, input().split())
    cnt = 0
    for i in range(1, t + 1):
        if i % a == 0:
            cnt += b
    print(cnt)

if __name__ == '__main__':
    main()
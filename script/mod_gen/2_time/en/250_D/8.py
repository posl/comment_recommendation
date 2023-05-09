def main():
    N = int(input())
    cnt = 0
    for i in range(2, 1000000):
        for j in range(i + 1, 1000000):
            if i * j * j * j > N:
                break
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
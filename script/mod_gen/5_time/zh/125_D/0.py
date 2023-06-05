def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in a:
        if i < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(sum(map(abs, a)))
    else:
        print(sum(map(abs, a)) - min(map(abs, a)) * 2)

if __name__ == '__main__':
    main()
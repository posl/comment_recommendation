def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 0:
            if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
                cnt += 1
    print(cnt)
main()

if __name__ == '__main__':
    main()
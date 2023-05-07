def main():
    S = input()
    cnt = 0
    for i in S:
        if i == "+":
            cnt += 1
        else:
            cnt -= 1
    print(cnt)

if __name__ == '__main__':
    main()
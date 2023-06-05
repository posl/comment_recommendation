def main():
    s = input()
    k = int(input())
    if k == 1:
        print(s[0])
        return
    i = 0
    while i < k:
        if s[i] == '1':
            i += 1
        else:
            break
    if i == k:
        print(1)
        return
    print(s[i])

if __name__ == '__main__':
    main()
def main():
    s = input()
    k = int(input())
    i = 0
    for i in range(k):
        if s[i] != '1':
            break
    if i == k:
        print(1)
    else:
        print(s[i])

if __name__ == '__main__':
    main()
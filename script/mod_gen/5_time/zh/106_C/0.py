def main():
    s = input()
    k = int(input())
    l = len(s)
    if l == 1:
        print(s)
    elif l == 2:
        if k == 1:
            print(s[0])
        else:
            print(s[1])
    else:
        for i in range(k):
            if s[i] != '1':
                print(s[i])
                break
            elif i == k-1:
                print('1')

if __name__ == '__main__':
    main()
def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            break
        if i == k-1:
            print('1')

if __name__ == '__main__':
    main()
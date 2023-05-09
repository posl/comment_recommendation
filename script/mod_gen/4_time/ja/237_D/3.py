def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(1,n):
        if s[i-1] == 'L':
            a.insert(0,i)
        else:
            a.append(i)
    print(*a)

if __name__ == '__main__':
    main()
def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == 'L':
            a.insert(0, i+1)
        else:
            a.append(i+1)
    print(*a)

if __name__ == '__main__':
    main()
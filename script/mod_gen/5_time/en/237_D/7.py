def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(1,n):
        if s[i-1] == "R":
            a.append(i)
        else:
            a.insert(0,i)
    print(*a)

if __name__ == '__main__':
    main()
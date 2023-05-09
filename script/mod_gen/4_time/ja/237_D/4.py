def main():
    n = int(input())
    s = input()
    a = [0]
    for i in range(n):
        if s[i] == "L":
            a.insert(i,a[i])
        else:
            a.insert(i+1,a[i]+1)
    print(" ".join(map(str,a)))
main()

if __name__ == '__main__':
    main()
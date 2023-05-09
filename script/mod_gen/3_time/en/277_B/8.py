def main():
    n = int(input())
    l = [input() for _ in range(n)]
    if len(set(l)) == n:
        if all([i[0] in "HDCS" and i[1] in "A23456789TJQK" for i in l]):
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()
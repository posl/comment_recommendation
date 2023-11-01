def main():
    n = int(input())
    a = [input() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == "W" and a[j][i] != "L":
                print("incorrect")
                return
            elif a[i][j] == "L" and a[j][

if __name__ == '__main__':
    main()
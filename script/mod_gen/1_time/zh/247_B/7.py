def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input().split())
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if a[i][0] == a[j][0] or a[i][1] == a[j][1]:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()
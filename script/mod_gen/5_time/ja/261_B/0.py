def main():
    n = int(input())
    a = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] != a[j][i]:
                print("incorrect")
                return
    print("correct")
main()

if __name__ == '__main__':
    main()
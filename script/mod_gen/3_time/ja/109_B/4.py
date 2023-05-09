def main():
    n = int(input())
    w = []
    w.append(input())
    for i in range(1, n):
        w.append(input())
        if w[i-1][-1] != w[i][0] or w.count(w[i]) > 1:
            print("No")
            return
    print("Yes")

if __name__ == '__main__':
    main()
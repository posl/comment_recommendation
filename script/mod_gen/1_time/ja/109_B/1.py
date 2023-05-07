def main():
    n = int(input())
    w = [input() for _ in range(n)]
    if len(set(w)) != n:
        print("No")
        return
    for i in range(1, n):
        if w[i][0] != w[i - 1][-1]:
            print("No")
            return
    print("Yes")
    return

if __name__ == '__main__':
    main()
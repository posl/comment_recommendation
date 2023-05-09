def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    if len(set(s) & set(t)) == 0:
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    main()
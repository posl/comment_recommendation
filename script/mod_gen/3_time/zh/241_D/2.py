def main():
    n = int(input())
    a = []
    for _ in range(n):
        q = input().split()
        if q[0] == '1':
            a.append(int(q[1]))
        elif q[0] == '2':
            a.sort(reverse=True)
            print(a[int(q[2])-1])
        else:
            a.sort()
            print(a[int(q[2])-1])
    return

if __name__ == '__main__':
    main()
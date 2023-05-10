def main():
    n = int(input())
    a = []
    for i in range(n):
        q = input().split()
        if q[0] == '1':
            a.append(int(q[1]))
        elif q[0] == '2':
            print(sorted(a, reverse=True)[int(q[2])-1])
        else:
            print(sorted(a)[int(q[2])-1])
    return
main()

if __name__ == '__main__':
    main()
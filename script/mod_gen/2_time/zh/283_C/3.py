def main():
    n = int(input())
    a = list(map(int,input().split()))
    q = int(input())
    for i in range(q):
        cmd = list(map(int,input().split()))
        if cmd[0] == 1:
            a[cmd[1]-1] = cmd[2]
        elif cmd[0] == 2:
            print(a[cmd[1]-1])

if __name__ == '__main__':
    main()
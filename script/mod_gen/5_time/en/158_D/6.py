def main():
    s = input()
    q = int(input())
    reverse = False
    head = []
    tail = []
    for _ in range(q):
        cmd = input().split()
        if cmd[0] == '1':
            reverse = not reverse
        else:
            if cmd[1] == '1':
                if reverse:
                    tail.append(cmd[2])
                else:
                    head.append(cmd[2])
            else:
                if reverse:
                    head.append(cmd[2])
                else:
                    tail.append(cmd[2])
    if reverse:
        s = s[::-1]
        head, tail = tail, head
    print(''.join(head) + s + ''.join(tail))

if __name__ == '__main__':
    main()
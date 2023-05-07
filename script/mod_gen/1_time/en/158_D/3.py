def main():
    S = input()
    Q = int(input())
    rev = False
    front = []
    back = []
    for i in range(Q):
        query = list(input().split())
        if query[0] == '1':
            rev = not rev
        else:
            if (query[1] == '1') ^ rev:
                front.append(query[2])
            else:
                back.append(query[2])
    front = ''.join(front)
    back = ''.join(back)
    if rev:
        print(back[::-1] + S[::-1] + front[::-1])
    else:
        print(front + S + back)

if __name__ == '__main__':
    main()
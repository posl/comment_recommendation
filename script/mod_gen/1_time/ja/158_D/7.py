def main():
    S = input()
    Q = int(input())
    rev = False
    front = []
    back = []
    for _ in range(Q):
        q = list(input().split())
        if q[0] == "1":
            rev = not rev
        else:
            if q[1] == "1":
                if rev:
                    back.append(q[2])
                else:
                    front.append(q[2])
            else:
                if rev:
                    front.append(q[2])
                else:
                    back.append(q[2])
    if rev:
        print("".join(list(reversed(front))+list(reversed(S))+list(reversed(back))))
    else:
        print("".join(front+S+back))

if __name__ == '__main__':
    main()
def main():
    S = input()
    Q = int(input())
    query = [input().split() for _ in range(Q)]
    reverse = False
    front = []
    back = []
    for q in query:
        if q[0] == '1':
            reverse = not reverse
        else:
            if q[1] == '1':
                if reverse:
                    back.append(q[2])
                else:
                    front.append(q[2])
            else:
                if reverse:
                    front.append(q[2])
                else:
                    back.append(q[2])
    if reverse:
        front, back = back[::-1], front[::-1]
    print(''.join(front + list(S) + back))

if __name__ == '__main__':
    main()
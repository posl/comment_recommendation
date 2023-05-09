def main():
    s = input()
    q = int(input())
    is_reverse = False
    front = ''
    back = ''
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            is_reverse = not is_reverse
        else:
            if query[1] == '1':
                if is_reverse:
                    back += query[2]
                else:
                    front += query[2]
            else:
                if is_reverse:
                    front += query[2]
                else:
                    back += query[2]
    if is_reverse:
        print(back[::-1] + s[::-1] + front)
    else:
        print(front[::-1] + s + back)

if __name__ == '__main__':
    main()
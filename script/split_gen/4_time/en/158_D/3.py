def main():
    s = input()
    q = int(input())
    reverse = False
    front = ''
    back = ''
    for _ in range(q):
        query = input().split()
        if query[0] == '1':
            reverse = not reverse
        else:
            if query[1] == '1':
                if reverse:
                    back += query[2]
                else:
                    front += query[2]
            else:
                if reverse:
                    front += query[2]
                else:
                    back += query[2]
    if reverse:
        print(back[::-1] + s[::-1] + front)
    else:
        print(front[::-1] + s + back)

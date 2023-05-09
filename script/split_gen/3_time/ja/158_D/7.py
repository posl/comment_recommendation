def main():
    s = input()
    q = int(input())
    querys = [input().split() for _ in range(q)]
    querys.reverse()
    reverse = False
    for query in querys:
        if query[0] == '1':
            reverse = not reverse
        else:
            if query[1] == '1':
                if reverse:
                    s += query[2]
                else:
                    s = query[2] + s
            else:
                if reverse:
                    s = query[2] + s
                else:
                    s += query[2]
    if reverse:
        s = s[::-1]
    print(s)

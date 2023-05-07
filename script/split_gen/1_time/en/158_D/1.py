def main():
    s = input()
    q = int(input())
    rev = False
    for i in range(q):
        t = list(map(str, input().split()))
        if t[0] == '1':
            rev = not rev
        else:
            if t[1] == '1':
                if rev:
                    s += t[2]
                else:
                    s = t[2] + s
            else:
                if rev:
                    s = t[2] + s
                else:
                    s += t[2]
    if rev:
        print(s[::-1])
    else:
        print(s)

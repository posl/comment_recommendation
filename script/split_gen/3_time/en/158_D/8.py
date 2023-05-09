def main():
    s = input()
    q = int(input())
    r = 0
    for i in range(q):
        t = input()
        if t == "1":
            r += 1
        else:
            t,f,c = t.split()
            if f == "1":
                if r % 2 == 0:
                    s = c + s
                else:
                    s = s + c
            else:
                if r % 2 == 0:
                    s = s + c
                else:
                    s = c + s
    if r % 2 == 1:
        s = s[::-1]
    print(s)

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    sn = set(s)
    for i in sn:
        if i[0] == "!":
            if i[1:] in sn:
                print(i[1:])
                return
    print("satisfiable")

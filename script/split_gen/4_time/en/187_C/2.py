def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = set()
    for i in range(n):
        if s[i][0] == "!":
            if s[i][1:] in t:
                print(s[i][1:])
                return
        else:
            if "!" + s[i] in t:
                print(s[i])
                return
        t.add(s[i])
    print("satisfiable")

def main():
    N = int(input())
    S = set()
    for i in range(N):
        s = input()
        if s[0] == "!":
            if s[1:] in S:
                print(s[1:])
                return
            else:
                S.add(s)
        else:
            if "!" + s in S:
                print(s)
                return
            else:
                S.add(s)
    print("satisfiable")

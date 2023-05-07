def resolve():
    from collections import defaultdict
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input()
        d[s] += 1
    for k, v in d.items():
        if k[0] == "!":
            if d[k[1:]] > 0:
                print(k[1:])
                exit()
        else:
            if d["!" + k] > 0:
                print(k)
                exit()
    print("satisfiable")

if __name__ == '__main__':
    resolve()
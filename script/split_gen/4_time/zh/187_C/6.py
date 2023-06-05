def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s = set(s)
    for i in s:
        if "!" + i in s:
            print(i)
            exit()
    print("satisfiable")

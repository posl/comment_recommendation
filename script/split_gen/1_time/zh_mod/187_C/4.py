def main():
    n = int(input())
    s = set()
    for _ in range(n):
        s.add(input())
    for i in s:
        if "!" + i in s:
            print(i)
            return
    print("satisfiable")

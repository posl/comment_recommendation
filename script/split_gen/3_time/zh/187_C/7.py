def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = set(s)
    for x in s:
        if '!' + x in s:
            print(x)
            return
    print('satisfiable')

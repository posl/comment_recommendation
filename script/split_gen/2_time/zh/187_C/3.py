def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = set(s)
    for i in s:
        if '!' + i in s:
            print(i)
            break
    else:
        print('satisfiable')

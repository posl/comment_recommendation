def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s_set = set(s)
    for i in s_set:
        if '!' + i in s_set:
            print(i)
            return
    print('satisfiable')

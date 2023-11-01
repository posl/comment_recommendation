def problem187c():
    n = int(input())
    s = [input() for _ in range(n)]
    s = set(s)
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                return i[1:]
    return 'satisfiable'

if __name__ == '__main__':
    problem187c()
def main():
    n = int(input())
    s = [input() for i in range(n)]
    s = set(s)
    for i in s:
        if i[0] == '!':
            if i[1:] in s:
                print(i[1:])
                exit()
        else:
            if ('!'+i) in s:
                print(i)
                exit()
    print('satisfiable')

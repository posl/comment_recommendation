def problem111_a():
    n = input()
    n = n.replace('1','2')
    n = n.replace('9','1')
    n = n.replace('2','9')
    print(n)

if __name__ == '__main__':
    problem111_a()
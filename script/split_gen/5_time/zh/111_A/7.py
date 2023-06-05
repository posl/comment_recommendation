def problem111_a():
    n = input()
    n = n.replace('1','2')
    n = n.replace('9','1')
    n = n.replace('2','9')
    print(n)

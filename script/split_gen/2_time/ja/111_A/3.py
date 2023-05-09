def main():
    n = input()
    n = n.replace('9', 'x')
    n = n.replace('1', '9')
    n = n.replace('x', '1')
    print(n)

def main():
    n = input()
    n = n.replace('1', 't')
    n = n.replace('9', '1')
    n = n.replace('t', '9')
    print(n)

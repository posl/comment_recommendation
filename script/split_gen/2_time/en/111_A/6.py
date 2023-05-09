def main():
    n = int(input())
    n = str(n)
    print(n.replace('9', 'x').replace('1', '9').replace('x', '1'))

def main():
    n = int(input())
    x = str(n)
    x = x.replace('9', 'x')
    x = x.replace('1', '9')
    x = x.replace('x', '1')
    print(x)
main()

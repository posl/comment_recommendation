def main():
    x = input()
    if '.' in x:
        print(x[0:x.find('.')])
    else:
        print(x)
main()

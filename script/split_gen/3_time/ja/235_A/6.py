def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c+a*100+b*10+c, a+c+c*100+a*10+b, b+c+c*100+a*10+b, sep=' + ')

def main():
    abc = input()
    a = abc[0]
    b = abc[1]
    c = abc[2]
    xyz = int(a+b+c) + int(b+c+a) + int(c+a+b)
    print(xyz)

def main():
    x = input()
    a,b = x.split()
    a = int(a)
    b = int(b)
    c = a + b
    d = a - b
    e = a * b
    print(max(c,d,e))

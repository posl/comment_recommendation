def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    m = min(a,b,c,d,e)
    print(4 + (n + m - 1) // m)

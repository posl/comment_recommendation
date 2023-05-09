def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    print(min(((a+9)//10)*10, ((b+9)//10)*10, ((c+9)//10)*10, ((d+9)//10)*10, ((e+9)//10)*10) + max(a, b, c, d, e))

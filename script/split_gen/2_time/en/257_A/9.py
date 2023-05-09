def main():
    n, x = map(int, input().split())
    a = 26*n
    b = n
    c = 26
    if x <= a:
        print(chr(65 + ((x-1)//b)))
    else:
        print(chr(65 + ((x-a-1)//c)))

def main():
    a,b,c = map(int,input().split())
    if a < 0 and c%2 == 0:
        a = abs(a)
    if b < 0 and c%2 == 0:
        b = abs(b)
    if pow(a,c) < pow(b,c):
        print("<")
    elif pow(a,c) > pow(b,c):
        print(">")
    else:
        print("=")

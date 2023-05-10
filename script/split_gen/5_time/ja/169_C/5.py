def main():
    a, b = map(str, input().split())
    a = int(a)
    b = int(float(b)*100)
    print(a*b//100)

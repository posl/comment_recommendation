def main():
    a, b = map(int, input().split())
    print(str(a)*b if str(a)*b < str(b)*a else str(b)*a)

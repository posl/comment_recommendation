def main():
    A,B,C = map(int,input().split())
    print(C-(A-B) if C-(A-B) > 0 else 0)

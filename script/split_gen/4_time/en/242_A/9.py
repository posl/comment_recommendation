def main():
    A,B,C,X = map(int, input().split())
    print((min(B,X)-A+1)/B if A <= X <= B else 0)

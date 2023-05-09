def main():
    A,B,C = map(int,input().split())
    print(max(10*A+B+C,10*B+A+C,10*C+A+B))

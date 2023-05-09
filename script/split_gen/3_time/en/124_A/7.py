def main():
    A,B = map(int,input().split())
    print(max(A+B,A-1,B-1))

def main():
    N = int(input())
    A = list(map(int,input().split()))
    print(" ".join(map(str,sorted(A,key = lambda x: -x))))

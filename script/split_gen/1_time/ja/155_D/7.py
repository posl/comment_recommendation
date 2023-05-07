def main():
    import sys
    input = sys.stdin.readline
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort()
    A = [abs(i) for i in A]
    A.sort()
    A = [0] + A

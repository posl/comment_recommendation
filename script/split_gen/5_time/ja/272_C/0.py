def main():
    N = int(input())
    A = list(map(int,input().split()))
    if len(A) == len(set(A)):
        print(-1)
    else:
        print(max(A) * 2)

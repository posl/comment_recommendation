def main():
    import sys
    #A, B, C = map(int, input().split())
    A, B, C = map(int, sys.stdin.readline().split())
    for i in range(A, B+1):
        if i % C == 0:
            print(i)
            return
    print(-1)
    return

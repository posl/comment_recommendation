def main():
    import sys
    h,a = map(int, sys.stdin.readline().split())
    print((h-1)//a+1)

def solution():
    n,x = map(int, raw_input().split())
    p = map(int, raw_input().split())
    print p.index(x)+1

if __name__ == '__main__':
    solution()
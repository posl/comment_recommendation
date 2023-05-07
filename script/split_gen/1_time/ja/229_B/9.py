def main():
    import sys
    input = sys.stdin.readline
    A,B = map(int,input().split())
    print('Hard' if len(str(A+B))>len(str(A)) else 'Easy')

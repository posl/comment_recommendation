def main():
    A,B = map(int,input().split())
    if A*1 <= B <= A*6:
        print('Yes')
    else:
        print('No')

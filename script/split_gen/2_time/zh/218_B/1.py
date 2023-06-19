def main():
    p=list(map(int,input().split()))
    a=[chr(96+i) for i in p]
    print(''.join(a))

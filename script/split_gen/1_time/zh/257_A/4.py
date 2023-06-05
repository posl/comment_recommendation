def main():
    N,X = map(int,input().split())
    print(chr(ord('A')+X//N-1),end='')

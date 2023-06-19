def main():
    N,X = map(int,input().split())
    if X%N == 0:
        print(chr(64+N))
    else:
        print(chr(64+X%N))

def main():
    N=int(input())
    S=input()
    for i in S:
        if ord(i)+N>ord("Z"):
            print(chr(ord(i)+N-26),end="")
        else:
            print(chr(ord(i)+N),end="")

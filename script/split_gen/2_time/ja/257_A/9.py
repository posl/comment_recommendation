def main():
    n,x = map(int,input().split())
    print(chr(64+n+(x-n)%26))

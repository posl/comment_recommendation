def main():
    n,x = map(int,input().split())
    if x <= n:
        print(chr(x + ord('A') - 1))
    else:
        print(chr((x - n - 1) % 26 + ord('A')))
main()

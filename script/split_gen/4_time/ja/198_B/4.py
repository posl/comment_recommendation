def main():
    N = int(input())
    if N == int(str(N)[::-1]):
        print('Yes')
    else:
        print('No')
main()

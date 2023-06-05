def main():
    a = int(input())
    b = list(map(int,input().split()))
    c = 0
    for i in b:
        c += 1/i
    print(1/c)
main()

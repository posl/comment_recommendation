def main():
    a,b = map(int, input().split())
    for p in range(1,1001):
        if int(p * 0.08) == a and int(p * 0.1) == b:
            print(p)
            return
    print(-1)
    return
main()

def main():
    k = int(input())
    num = 0
    for i in range(1,k+1):
        num = num*10+7
        num = num%k
        if num == 0:
            print(i)
            return
    print(-1)
    return
main()

def main():
    n = int(input())
    cnt = 0
    for i in range(1,n+1):
        if '7' not in str(i) and '7' not in oct(i):
            cnt += 1
    print(cnt)
main()

def main():
    N = int(input())
    ans = 0
    for i in range(1, 12):
        for j in range(10**(i-1), 10**i):
            if j > N:
                break
            if len(str(j))%2 == 0:
                if str(j)[:len(str(j))//2] == str(j)[len(str(j))//2:]:
                    ans += 1
    print(ans)
main()

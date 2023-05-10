def main():
    l = int(input())
    ans = 0
    for i in range(1, l-11):
        for j in range(i+1, l-i-10):
            ans += 1
    print(ans)
main()

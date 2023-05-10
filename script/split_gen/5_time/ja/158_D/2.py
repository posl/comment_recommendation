def main():
    s = input()
    q = int(input())
    ans = s
    for i in range(q):
        t = input().split()
        if t[0] == '1':
            ans = ans[::-1]
        else:
            if t[1] == '1':
                ans = t[2] + ans
            else:
                ans = ans + t[2]
    print(ans)
main()

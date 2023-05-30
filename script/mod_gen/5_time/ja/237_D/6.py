def main():
    n = int(input())
    s = input()
    ans = []
    ans.append(0)
    for i in range(n-1):
        if s[i] == "L":
            ans.insert(0,i+1)
        else:
            ans.append(i+1)
    print(*ans)
main()

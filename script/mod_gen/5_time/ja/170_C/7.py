def main():
    x,n = map(int,input().split())
    p = list(map(int,input().split()))
    ans = 0
    for i in range(x,101):
        if i not in p:
            ans = i
            break
    for i in range(x,0,-1):
        if i not in p:
            if ans == 0:
                ans = i
            else:
                if abs(x-i) <= abs(x-ans):
                    ans = i
                break
    print(ans)

if __name__ == '__main__':
    main()
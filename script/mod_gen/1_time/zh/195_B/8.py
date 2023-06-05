def main():
    a,b,w = map(int,input().split())
    w *= 1000
    ans = []
    for i in range(1,w+1):
        if a*i <= w <= b*i:
            ans.append(i)
    if len(ans) == 0:
        print("UNSATISFIABLE")
    else:
        print(min(ans),max(ans))

if __name__ == '__main__':
    main()
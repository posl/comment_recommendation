def main():
    a,b,w = map(int,input().split())
    ans = []
    for i in range(1,1001):
        if a*i <= w*1000 <= b*i:
            ans.append(i)
    if len(ans) == 0:
        print("UNSATISFIABLE")
    else:
        print(min(ans),max(ans))

if __name__ == '__main__':
    main()
def main():
    N,M = map(int,input().split())
    ans = []
    for i in range(1,M+1):
        for j in range(1,M+1):
            if i < j:
                ans.append(str(i)+" "+str(j))
    print("\n".join(ans))

if __name__ == '__main__':
    main()
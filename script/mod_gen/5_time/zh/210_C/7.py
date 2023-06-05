def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    #n,k = 7,3
    #c = [1,2,1,2,3,3,1]
    #n,k = 5,5
    #c = [4,4,4,4,4]
    #n,k = 10,6
    #c = [304621362,506696497,304621362,506696497,834022578,304621362,414720753,304621362,304621362,414720753]
    #print(n,k,c)
    ans = 0
    for i in range(n-k+1):
        tmp = len(set(c[i:i+k]))
        if tmp > ans:
            ans = tmp
    print(ans)

if __name__ == '__main__':
    main()
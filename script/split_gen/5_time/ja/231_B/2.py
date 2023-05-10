def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    #print(S)
    import itertools
    max = 0
    ans = ""
    for i in itertools.groupby(S):
        #print(i)
        #print(list(i[1]))
        if max < len(list(i[1])):
            max = len(list(i[1]))
            ans = i[0]
    print(ans)
main()

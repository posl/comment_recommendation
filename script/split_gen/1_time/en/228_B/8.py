def main():
    #input
    N, X = map(int, input().split())
    As = list(map(int, input().split()))
    #compute
    dic = {}
    dic[X] = 1
    for i in range(N):
        X = As[X-1]
        if X in dic.keys():
            break
        dic[X] = 1
    #output
    print(len(dic))

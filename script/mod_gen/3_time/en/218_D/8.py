def main():
    N = int(input())
    x,y = [],[]
    for i in range(N):
        x_i,y_i = map(int,input().split())
        x.append(x_i)
        y.append(y_i)
    x_set = list(set(x))
    y_set = list(set(y))
    x_set.sort()
    y_set.sort()
    x_dict = {x_set[i]:i for i in range(len(x_set))}
    y_dict = {y_set[i]:i for i in range(len(y_set))}
    x_count = [0 for i in range(len(x_set))]
    y_count = [0 for i in range(len(y_set))]
    for i in range(N):
        x_count[x_dict[x[i]]] += 1
        y_count[y_dict[y[i]]] += 1
    ans = 0
    for i in range(len(x_set)):
        for j in range(i+1,len(x_set)):
            for k in range(len(y_set)):
                for l in range(k+1,len(y_set)):
                    num = 0
                    for m in range(N):
                        if x_dict[x[m]] >= i and x_dict[x[m]] < j and y_dict[y[m]] >= k and y_dict[y[m]] < l:
                            num += 1
                    if num > 1:
                        ans += num*(num-1)//2
    print(ans)

if __name__ == '__main__':
    main()
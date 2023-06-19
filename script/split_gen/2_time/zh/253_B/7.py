def main():
    h,w = map(int, input().split())
    s = [input() for _ in range(h)]
    #print(s)
    min_ = h+w
    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                #print(i,j)
                for k in range(h):
                    for l in range(w):
                        if s[k][l] == 'o' and (i != k or j != l):
                            #print(k,l)
                            min_ = min(min_, abs(i-k)+abs(j-l))
    print(min_ - 1)

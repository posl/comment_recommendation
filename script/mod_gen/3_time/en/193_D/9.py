def  main():
    k =  int (input())
    s = input()
    t = input()
    s = s[:-1]
    t = t[:-1]
    #print(s)
    #print(t)
    takahashi = [0] * 10
    aoki = [0] * 10
    for i in s:
        takahashi[ int (i)] +=  1 
    for i in t:
        aoki[ int (i)] +=  1 
    #print(takahashi)
    #print(aoki)
    takahashi_score =  0 
    aoki_score =  0 
    for i in range( 1 , 10):
        takahashi_score += i *  10 ** takahashi[i]
        aoki_score += i *  10 ** aoki[i]
    #print(takahashi_score)
    #print(aoki_score)
    takahashi_win =  0 
    for i in range( 1 , 10):
        for j in range( 1 , 10):
            takahashi_score_tmp = takahashi_score
            aoki_score_tmp = aoki_score
            if takahashi[i] < k and aoki[j] < k:
                takahashi_score_tmp += i *  10 ** takahashi[i]
                aoki_score_tmp += j *  10 ** aoki[j]
                if takahashi_score_tmp > aoki_score_tmp:
                    if i == j:
                        takahashi_win += (k - takahashi[i]) * (k - aoki[j] -  1 )
                    else :
                        takahashi_win += (k - takahashi[i]) * (k - aoki[j])
    #print(takahashi_win)
    print(takahashi_win / ((k *  9 ) * (k *  9  -  1 )))

if __name__ == '__main__':
    ()
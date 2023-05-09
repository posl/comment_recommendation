def dice(n,k,p):
    #n - number of dice
    #k - number of dice to be chosen
    #p - list of sides of each die
    #return - max expected sum of k dice
    #print("n=",n,"k=",k,"p=",p)
    #print("p[0:k]=",p[0:k])
    #print("sum(p[0:k])=",sum(p[0:k]))
    max_expected_sum = sum(p[0:k])
    for i in range(1,n-k+1):
        #print("i=",i)
        #print("p[i:i+k]=",p[i:i+k])
        #print("sum(p[i:i+k])=",sum(p[i:i+k]))
        if sum(p[i:i+k]) > max_expected_sum:
            max_expected_sum = sum(p[i:i+k])
    return max_expected_sum

if __name__ == '__main__':
    dice()
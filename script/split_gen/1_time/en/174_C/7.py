def main():
    #input
    K = int(input())
    #output
    if K%2==0 or K%5==0:
        print(-1)
    else:
        #process
        count = 1
        mod = 7%K
        while mod!=0:
            mod = (mod*10+7)%K
            count += 1
        print(count)

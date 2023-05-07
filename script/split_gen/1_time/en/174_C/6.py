def main():
    #input
    K = int(input())
    
    #exception
    if K % 2 == 0:
        print(-1)
        return
    
    #count
    count = 0
    n = 7
    while n % K != 0:
        n = n * 10 + 7
        count += 1
        if count > K:
            print(-1)
            return
    
    #output
    print(count + 1)
    
    return

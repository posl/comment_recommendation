def main():
    #K = int(input())
    K = 101
    #K = 2
    #K = 999983
    #print(K)
    #print(type(K))
    if K%2 == 0 or K%5 == 0:
        print(-1)
    else:
        i = 1
        while True:
            if 7*i%K == 0:
                print(i)
                break
            i += 1

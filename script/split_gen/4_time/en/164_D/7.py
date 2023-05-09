def main():
    s = input()
    n = len(s)
    #print(n)
    #print(s)
    count = 0
    for i in range(0,n):
        for j in range(i,n):
            #print(i,j)
            #print(s[i:j+1])
            if int(s[i:j+1]) % 2019 == 0:
                count += 1
                #print("count",count)
    print(count)

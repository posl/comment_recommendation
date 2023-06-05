def main():
    N = int(input())
    #N = 963761198400
    count = 0
    for i in range(1,int(N/2)+2):
        #print(i)
        if i % 2 == 0:
            if N % i == int(i/2):
                #print(i)
                count += 1
        else:
            if N % i == 0:
                #print(i)
                count += 1
    print(count * 2)

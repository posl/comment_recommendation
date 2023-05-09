def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i%2==1:
            if len([x for x in range(1,i+1) if i%x==0])==8:
                count+=1
    print(count)

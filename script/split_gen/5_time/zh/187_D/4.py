def main():
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        line=input()
        a.append(int(line.split()[0]))
        b.append(int(line.split()[1]))
    #print(a)
    #print(b)
    count=0
    for i in range(n):
        if a[i]>b[i]:
            count+=1
    print(count)

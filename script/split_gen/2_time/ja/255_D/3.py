def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    #print(n, q, a, x)
    #a.sort()
    #print(a)
    #print(x)
    #print()
    for i in range(q):
        #print("x[i]={}".format(x[i]))
        #print("a={}".format(a))
        #print("x[i]={}".format(x[i]))
        #print("a={}".format(a))
        #print("a[0]={}".format(a[0]))
        #print("a[n-1]={}".format(a[n-1]))
        #print("a[n]={}".format(a[n]))
        #print()
        if x[i] < a[0]:
            print(a[0]-x[i])
        elif x[i] > a[n-1]:
            print(x[i]-a[n-1])
        else:
            #print("a={}".format(a))
            #print("x[i]={}".format(x[i]))
            #print("a[0]={}".format(a[0]))
            #print("a[n-1]={}".format(a[n-1]))
            #print("a[n]={}".format(a[n]))
            #print()
            j = 0
            k = n
            while k-j > 1:
                #print("j={}, k={}".format(j, k))
                m = (j+k)//2
                #print("m={}".format(m))
                if a[m] == x[i]:
                    #print("a[m] == x[i]")
                    print(0)
                    break
                elif a[m] < x[i]:
                    #print("a[m] < x[i]")
                    j = m
                else:
                    #print("a[m] > x[i]")
                    k = m
            else:
                #print("j={}, k={}".format(j, k))
                #print("a[j]={}, a[k]={}".format(a[j], a[k]))
                #print("x[i]={}".format(x[i]))
                print(min(x[i]-a[j], a[k]-x[i]))

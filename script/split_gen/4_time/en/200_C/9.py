def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    #a.sort()
    #print(a)
    #print(len(a))
    #for i in range(len(a)):
    #    print(a[i])
    #for i in range(len(a)):
    #    for j in range(len(a)):
    #        print(a[i], a[j])
    count = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if i < j and (a[i] - a[j]) % 200 == 0:
                count += 1
                #print(a[i], a[j])
    print(count)

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    a.sort(reverse = True)
    b.sort(reverse = True)
    #print(a)
    #print(b)
    takahashi = 0
    aoki = 0
    for i in range(n):
        #print("aoki = ", aoki)
        #print("takahashi = ", takahashi)
        if aoki >= takahashi:
            takahashi += b[i]
        else:
            aoki += a[i]
        #print("aoki = ", aoki)
        #print("takahashi = ", takahashi)
        if aoki > takahashi:
            print(i+1)
            exit()
main()

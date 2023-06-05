def main():
    num = input()
    num = num.split()
    n = int(num[0])
    q = int(num[1])
    a = input()
    a = a.split()
    a = [int(x) for x in a]
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    b = []
    for i in range(n-1):
        b.append(a[i+1]-a[i]-1)
    b.insert(0,a[0]-1)
    for i in range(q):
        for j in range(n):
            if k[i] <= b[j]:
                print(a[j]+k[i])
                break
            else:
                k[i] = k[i]-b[j]

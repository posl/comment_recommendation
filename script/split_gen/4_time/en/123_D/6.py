def main():
    x,y,z,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    abc = []
    for i in range(x):
        for j in range(y):
            abc.append(a[i]+b[j])
    abc.sort(reverse=True)
    abc = abc[:k]
    abcc = []
    for i in range(len(abc)):
        for j in range(z):
            abcc.append(abc[i] + c[j])
    abcc.sort(reverse=True)
    abcc = abcc[:k]
    for i in range(k):
        print(abcc[i])

def main():
    #input
    a = list(map(int, input().split()))
    #compute
    for i in range(3):
        a = [a[a[i]] for i in range(10)]
    #output
    print(a[0])

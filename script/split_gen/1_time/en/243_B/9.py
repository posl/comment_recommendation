def main():
    #input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #compute
    a_b = 0
    b_b = 0
    for i in range(n):
        if a[i] == b[i]:
            a_b += 1
    for i in range(n):
        for j in range(n):
            if a[i] == b[j] and i != j:
                b_b += 1
    #output
    print(a_b)
    print(b_b)

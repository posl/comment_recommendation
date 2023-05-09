def main():
    n = int(input())
    a = list(map(int, input().split()))
    #print(n)
    #print(a)
    gcd_degree = 0
    gcd_degree_max = 0
    gcd_degree_max_num = 0
    for i in range(2, 1001):
        for j in range(0, n):
            if a[j] % i == 0:
                gcd_degree += 1
        if gcd_degree > gcd_degree_max:
            gcd_degree_max = gcd_degree
            gcd_degree_max_num = i
        gcd_degree = 0
    print(gcd_degree_max_num)

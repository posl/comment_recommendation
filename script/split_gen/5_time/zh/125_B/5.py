def main():
    n = int(input())
    v = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    #print(n,v,c)
    v_sum = 0
    c_sum = 0
    for i in range(n):
        v_sum += v[i]
        c_sum += c[i]
    #print(v_sum,c_sum)
    print(v_sum - c_sum)

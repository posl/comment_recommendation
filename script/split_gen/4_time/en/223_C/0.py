def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    #print(a)
    #print(b)
    flame = 0
    for i in range(n):
        flame += a[i]/b[i]
    #print(flame)
    flame /= 2
    #print(flame)
    dist = 0
    for i in range(n):
        if flame > a[i]/b[i]:
            dist += a[i]
        else:
            dist += flame*b[i]
            break
    print(dist)

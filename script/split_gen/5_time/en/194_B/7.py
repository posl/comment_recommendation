def main():
    #input
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    #process
    min_time = 10**10
    for i in range(n):
        for j in range(n):
            if i == j:
                time = a[i] + b[i]
            else:
                time = max(a[i], b[j])
            if time < min_time:
                min_time = time
    #output
    print(min_time)

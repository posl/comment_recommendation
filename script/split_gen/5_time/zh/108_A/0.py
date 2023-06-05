def problems108_a():
    k = int(input())
    if k < 2 or k > 100:
        return
    print(int(k/2) * int((k+1)/2))

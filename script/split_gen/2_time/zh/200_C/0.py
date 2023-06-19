def find_pairs(a):
    pairs = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if (a[i] - a[j]) % 200 == 0:
                pairs += 1
    return pairs

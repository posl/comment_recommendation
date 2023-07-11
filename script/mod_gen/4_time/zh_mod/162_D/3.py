def count_triples(s):
    count = 0
    n = len(s)
    for i in range(n-2):
        for j in range(i+1,n-1):
            k = j + (j-i)
            if k < n:
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k]:
                    count += 1
    return count

if __name__ == '__main__':
    count_triples()
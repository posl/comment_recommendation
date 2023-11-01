def count_triad(s):
    n = len(s)
    c = 0
    for i in range(0, n):
        for j in range(i+1, n):
            k = 2*j - i
            if k < n:
                if s[i] != s[j] and s[i] !=

if __name__ == '__main__':
    count_triad()
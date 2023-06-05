def get_num_of_triple(s):
    n = len(s)
    num = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j - i != k - j:
                    num += 1
    return num

if __name__ == '__main__':
    get_num_of_triple()
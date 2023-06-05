def find_3tuples(string):
    N = len(string)
    count = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                if string[i] != string[j] and string[i] != string[k] and string[j] != string[k]:
                    if (j-i) != (k-j):
                        count += 1
    return count

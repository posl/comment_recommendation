def print_answer(N, A):
    #print(N)
    #print(A)
    d = {}
    for a in A:
        if a in d:
            d[a] += 1
        else:
            d[a] = 1
    #print(d)
    for k in d:
        if d[k] % 2 == 1:
            print(k)
            break

if __name__ == '__main__':
    print_answer()
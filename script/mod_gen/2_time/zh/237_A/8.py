def max_xor(a):
    return max([a[i]^a[j] for i in range(len(a)) for j in range(i+1,len(a))])

if __name__ == '__main__':
    max_xor()
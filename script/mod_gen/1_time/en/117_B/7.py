def polygon(N, L):
    L.sort()
    if L[-1] < sum(L[:-1]):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    polygon()
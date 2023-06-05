def countTriplets(s):
    # Complete this function
    total = 0
    for i in range(len(s)-2):
        for j in range(i+1,len(s)-1):
            for k in range(j+1,len(s)):
                if s[i] != s[j] and s[i] != s[k] and s[j] != s[k] and j-i != k-j:
                    total += 1
    return total

if __name__ == '__main__':
    countTriplets()
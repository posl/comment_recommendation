def permute(s, k):
    #Base Case
    if len(s) == 1:
        return s
    #Recursion
    else:
        n = len(s)
        #Number of permutations of the string s[1:]
        p = factorial(n-1)
        #Find the index of the first character in the permutation
        i = (k-1)//p
        #Find the character in the permutation
        c = s[i]
        #Remove the character from the string
        s = s[:i] + s[i+1:]
        #Find the k-th permutation of the string s[1:]
        k = k - i*p
        return c + permute(s, k)

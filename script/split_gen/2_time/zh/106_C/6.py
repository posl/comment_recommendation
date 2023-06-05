def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    #print(len(s))
    if len(s) >= k:
        print(s[k-1])
    else:
        #print("here")
        #print(len(s))
        #print(k)
        #print(k % len(s))
        print(s[k % len(s) - 1])
    return 0

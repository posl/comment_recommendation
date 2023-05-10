def main():
    n = int(input())
    s = input()
    #print(n, s)
    for i in range(1, n):
        #print(i)
        count = 0
        for j in range(0, n-i):
            #print(j)
            if s[j] != s[j+i]:
                count += 1
        print(count)
    return

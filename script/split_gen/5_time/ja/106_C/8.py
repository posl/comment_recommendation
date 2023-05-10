def main():
    s = input()
    k = int(input())
    n = len(s)
    #print(s)
    #print(k)
    #print(n)
    #print(s[0])
    #print(s[1])
    #print(s[2])
    #print(s[3])
    for i in range(n):
        if i == k-1:
            print(s[i])
            break

def main():
    s = input()
    k = int(input())
    #print(s)
    #print(k)
    #print(len(s))
    for i in range(k):
        if i == k-1:
            print(s[0])
        if s[0] == '1':
            s = s[1:]
        else:
            s = s[0] + str(int(s[0])-1) + s[1:]

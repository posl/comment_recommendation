def main():
    s = input()
    t = input()
    #print(s,t)
    count = 0
    for i in range(len(s)-len(t)+1):
        #print(i)
        #print(s[i:i+len(t)])
        for j in range(len(t)):
            if s[i+j] != t[j]:
                count += 1
    print(count)
main()

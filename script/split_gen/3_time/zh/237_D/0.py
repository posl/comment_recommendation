def main():
    n = int(input())
    s = input()
    #print(n,s)
    a = [0]
    for i in range(1,n+1):
        if s[i-1] == 'L':
            a.insert(0,i)
        else:
            a.append(i)
    print(*a)

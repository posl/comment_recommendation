def main():
    n,w = map(int,input().split())
    time = [0] * (2*10**5 + 1)
    for i in range(n):
        s,t,p = map(int,input().split())
        time[s] += p
        time[t] -= p
    for i in range(1,2*10**5 + 1):
        time[i] += time[i-1]
    for i in range(2*10**5 + 1):
        if time[i] > w:
            print("No")
            exit()
    print("Yes")
main()

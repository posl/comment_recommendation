def main():
    N = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    #Snuke's next transaction time
    next_time = [0]*N
    #Snuke's next transaction type
    next_type = [0]*N
    #Snuke's next transaction target
    next_target = [0]*N
    #Snuke's next transaction time is Takahashi's
    for i in range(N):
        next_time[i] = T[i]
        next_type[i] = 0
        next_target[i] = i
    #Snuke's next transaction time is Snuke's
    for i in range(N):
        j = next_target[i]
        if next_time[j] > next_time[i] + S[i]:
            next_time[j] = next_time[i] + S[i]
            next_type[j] = 1
            next_target[j] = (i+1)%N
    #print(next_time)
    #print(next_type)
    #print(next_target)
    for i in range(N):
        print(next_time[i])

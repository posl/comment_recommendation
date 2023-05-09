def main():
    N = int(input())
    jump = [None]*N
    for i in range(N):
        x,y,p = map(int,input().split())
        jump[i] = [x,y,p]
    
    #print(jump)
    #print(N)
    s = 0
    while True:
        count = 0
        for i in range(N):
            for j in range(N):
                if i != j:
                    if jump[i][2]*s >= abs(jump[i][0]-jump[j][0]) + abs(jump[i][1]-jump[j][1]):
                        count += 1
        if count == N*(N-1):
            print(s)
            break
        else:
            s += 1

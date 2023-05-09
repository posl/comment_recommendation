def main():
    N, A, B = map(int, input().split())
    S = input()
    S = S + S
    #print(S)
    #Sの中で、S[i] == S[i+N]の数を数える
    cnt = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt += 1
    #print(cnt)
    #Sの中で、S[i] == S[i+N]の数を数える
    cnt2 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt2 += 1
    #print(cnt2)
    #Sの中で、S[i] == S[i+N]の数を数える
    cnt3 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt3 += 1
    #print(cnt3)
    #A円で一回操作した時に、Sの中で、S[i] == S[i+N]の数を数える
    cnt4 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt4 += 1
    #print(cnt4)
    #A円で一回操作した時に、Sの中で、S[i] == S[i+N]の数を数える
    cnt5 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt5 += 1
    #print(cnt5)
    #A円で一回操作した時に、Sの中で、S[i] == S[i+N]の数を数える
    cnt6 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt6 += 1
    #print(cnt6)
    #A円で一回操作した時に、Sの中で、S[i] == S[i+N]の数を数える
    cnt7 = 0
    for i in range(N):
        if S[i] == S[i+N]:
            cnt7 += 1
    #print(cnt7)
    #A円で一回操作した時に、Sの中で、

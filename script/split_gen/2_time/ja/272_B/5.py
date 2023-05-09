def main():
    N, M = list(map(int, input().split()))
    #N人の人が、M回の舞踏会に参加したかどうかを記録する
    #人は1からNまでの番号がついている
    #参加した場合は1、参加していない場合は0
    people = [[0] * M for i in range(N)]
    for i in range(M):
        a = list(map(int, input().split()))
        for j in range(a[0]):
            people[a[j+1]-1][i] = 1
    #print(people)
    for i in range(N):
        for j in range(i+1, N):
            #print(i, j)
            for k in range(M):
                if people[i][k] == 1 and people[j][k] == 1:
                    print("Yes")
                    return
    print("No")

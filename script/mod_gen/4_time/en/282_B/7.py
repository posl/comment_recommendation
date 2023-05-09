def count_solved_problems(s):
    count = 0
    for i in s:
        if i == 'o':
            count += 1
    return count
N, M = map(int, input().split())
S = []
for i in range(N):
    S.append(input())
#print(S)
#print(count_solved_problems(S[0]))
#print(count_solved_problems(S[1]))
#print(count_solved_problems(S[2]))
#print(count_solved_problems(S[3]))
#print(count_solved_problems(S[4]))
count = 0
for i in range(N):
    for j in range(i+1, N):
        if count_solved_problems(S[i]) + count_solved_problems(S[j]) == M:
            count += 1
print(count)

if __name__ == '__main__':
    count_solved_problems()
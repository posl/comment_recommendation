def change_handle(N, S, T):
    for i in range(N):
        for j in range(N):
            if S[i] == T[j]:
                if i == j:
                    continue
                else:
                    return 'No'
    return 'Yes'

if __name__ == '__main__':
    change_handle()
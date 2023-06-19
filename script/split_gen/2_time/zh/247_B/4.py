def solution(n, names):
    for i in range(n):
        for j in range(n):
            if i != j:
                if names[i][0] == names[j][0] or names[i][1] == names[j][1]:
                    return 'Yes'
    return 'No'

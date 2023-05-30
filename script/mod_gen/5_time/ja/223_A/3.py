def judge(X):
    if X%100 == 0 and X != 0:
        return "Yes"
    else:
        return "No"
X = int(input())
print(judge(X))

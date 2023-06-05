def happy_people(S):
    n = len(S)
    happy = 0
    for i in range(n-1):
        if S[i] == S[i+1]:
            happy += 1
    return happy

if __name__ == '__main__':
    happy_people()
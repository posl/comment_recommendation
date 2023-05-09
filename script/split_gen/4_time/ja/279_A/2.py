def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == 'v' and i != len(S) - 1 and S[i+1] == 'w':
            count += 1
    print(count)

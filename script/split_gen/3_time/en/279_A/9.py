def main():
    S = input()
    #print(S)
    #print(len(S))
    count = 0
    for i in range(0, len(S)):
        if S[i] == 'v':
            count += 1
    print(count * (count - 1) // 2)

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if i % 2 == 0 and S[i] == '1':
            count += 1
        elif i % 2 == 1 and S[i] == '0':
            count += 1
    print(count)

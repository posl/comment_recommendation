def main():
    S = input()
    if S[0] == '0':
        print('No')
    else:
        for i in range(1,11):
            if S[i] == '1':
                for j in range(i+1,11):
                    if S[j] == '1':
                        print('Yes')
                        return
        print('No')
        return

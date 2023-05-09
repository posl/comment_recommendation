def main():
    S = input()
    T = 'o'*10**5 + 'x'*10**5 + 'o'*10**5
    if S in T:
        print('Yes')
    else:
        print('No')

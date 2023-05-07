def main():
    N = input()
    for i in range(len(N)):
        if N[i] != N[-i-1]:
            print('No')
            return
    print('Yes')

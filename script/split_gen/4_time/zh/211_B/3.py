def main():
    S = []
    for i in range(4):
        S.append(input())
    if 'H' in S and '2B' in S and '3B' in S and 'HR' in S:
        print('Yes')
    else:
        print('No')

def main():
    S = input().split()
    T = input().split()
    if len(set(S)) == len(set(T)) == 3:
        print('Yes')
    else:
        print('No')

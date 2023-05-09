def main():
    # input
    N = int(input())
    names = []
    for i in range(N):
        names.append(input())
    names.sort()
    # compute
    # output
    for i in range(1,N):
        if names[i] == names[i-1]:
            print('Yes')
            break
    else:
        print('No')

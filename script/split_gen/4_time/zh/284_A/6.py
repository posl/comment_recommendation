def main():
    N = int(input())
    list = []
    for i in range(N):
        list.append(input())
    list.reverse()
    print('\n'.join(list))

def read_input():
    n = int(input())
    mountains = []
    for i in range(n):
        s, t = input().split()
        mountains.append((s, int(t)))
    return mountains

if __name__ == '__main__':
    read_input()
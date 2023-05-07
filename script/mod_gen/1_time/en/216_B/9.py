def get_input():
    n = int(input())
    names = []
    for i in range(n):
        names.append(input())
    return names

if __name__ == '__main__':
    get_input()
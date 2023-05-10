def main():
    n = int(input())
    l = []
    for i in range(1, 2**16):
        if n & i == i:
            l.append(i)
    l.sort()
    for i in l:
        print(i)

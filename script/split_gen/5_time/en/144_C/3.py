def main():
    N = int(input())
    i = 1
    j = 1
    count = 0
    while i*j < N:
        if i < j:
            i += 1
        else:
            j += 1
        count += 1
    print(count)

def main():
    x = [int(x) for x in input().split()]
    for i in range(len(x)):
        if x[i] == 0:
            print(i+1)
            break

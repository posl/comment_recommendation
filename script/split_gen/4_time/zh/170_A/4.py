def main():
    x = input().split()
    x = [int(i) for i in x]
    for i in range(5):
        if x[i] == 0:
            print(i+1)
            break

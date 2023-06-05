def main():
    inList = input().split()
    r = int(inList[0])
    D = int(inList[1])
    x = int(inList[2])
    for i in range(10):
        x = r * x - D
        print(x)

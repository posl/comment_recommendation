def main():
    #read input
    line = input()
    num = line.split(" ")
    n = int(num[0])
    a = int(num[1])
    b = int(num[2])
    #calculate
    train = a*n
    taxi = b
    if train > taxi:
        print(taxi)
    else:
        print(train)

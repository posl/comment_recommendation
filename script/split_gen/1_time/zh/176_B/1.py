def main():
    #n = int(input())
    n = input()
    #print(n)
    sum = 0
    for i in range(len(n)):
        sum += int(n[i])
    if sum % 9 == 0:
        print("Yes")
    else:
        print("No")

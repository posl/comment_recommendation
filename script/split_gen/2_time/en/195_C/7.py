def main():
    N = int(input())
    digit = len(str(N))
    #print(digit)
    if digit <= 3:
        print(0)
    elif digit == 4:
        print(N-999)
    else:
        sum = 0
        for i in range(4,digit+1):
            #print(i)
            sum += 3*(10**(i-1)-10**(i-4))
        print(sum)

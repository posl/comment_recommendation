def main():
    k = int(input()) #k is the multiple that Takahashi the Jumbo wants to achieve
    a, b = map(int, input().split()) #a and b are the range of the carry distance that Takahashi the Jumbo can make
    if a % k == 0 or b % k == 0: #if a or b is a multiple of k
        print('OK') #print OK
    else: #if a and b are not multiples of k
        print('NG') #print NG

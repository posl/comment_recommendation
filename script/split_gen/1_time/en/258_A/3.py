def main():
    #Enter your code here. Read input from STDIN. Print output to STDOUT
    K = int(input())
    HH = 21
    MM = 0
    MM += K
    if MM >= 60:
        HH += MM // 60
        MM = MM % 60
    if HH >= 24:
        HH = HH % 24
    if HH < 10:
        HH = '0' + str(HH)
    if MM < 10:
        MM = '0' + str(MM)
    print(str(HH)+':'+str(MM))

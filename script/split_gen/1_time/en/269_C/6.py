def main():
    N = int(input())
    #print(N)
    binN = bin(N)[2:]
    #print(binN)
    lenN = len(binN)
    #print(lenN)
    for i in range(2**(lenN)):
        binI = bin(i)[2:]
        lenI = len(binI)
        if binI.count('1') <= binN.count('1'):
            if lenI < lenN:
                binI = '0'*(lenN-lenI) + binI
            for j in range(lenN):
                if binN[j] == '1' and binI[j] == '1':
                    continue
                elif binN[j] == '1' and binI[j] == '0':
                    break
            else:
                print(i)

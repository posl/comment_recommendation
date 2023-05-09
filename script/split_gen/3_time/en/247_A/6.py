def main():
    S = input()
    #print(S)
    result = ''
    for i in range(0,4):
        if i == 3:
            result = result + '0'
        else:
            result = result + S[i]
    print(result)

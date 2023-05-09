def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    #print(S.count('"'))
    #print(S.count('"') % 2)
    if S.count('"') % 2 != 0:
        print("error")
        return
    #print(S.count(','))
    #print(S.count('"') // 2)
    #print(S.count(',') - S.count('"') // 2)
    #print(S.replace(',', '.', S.count(',') - S.count('"') // 2))
    print(S.replace(',', '.', S.count(',') - S.count('"') // 2))

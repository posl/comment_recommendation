def get_name_by_num(num):
    #第一步，计算num的位数
    #位数为1
    if num <= 26:
        return chr(96+num)
    #位数为2
    if num <= 702:
        if num % 26 == 0:
            return chr(96+num//26-1) + chr(122)
        else:
            return chr(96+num//26) + chr(96+num%26)
    #位数为3
    if num <= 18278:
        if num % 702 == 0:
            return chr(96+num//702-1) + chr(122) + chr(122)
        elif num % 26 == 0:
            return chr(96+num//702) + chr(96+num%702//26-1) + chr(122)
        else:
            return chr(96+num//702) + chr(96+num%702//26) + chr(96+num%26)
    #位数为4
    if num <= 475254:
        if num % 18278 == 0:
            return chr(96+num//18278-1) + chr(122) + chr(122) + chr(122)
        elif num % 702 == 0:
            return chr(96+num//18278) + chr(96+num%18278//702-1) + chr(122) + chr(122)
        elif num % 26 == 0:
            return chr(96+num//18278) + chr(96+num%18278//702) + chr(96+num%702//26-1) + chr(122)
        else:
            return chr(96+num//18278) + chr(96+num%18278//702) + chr(96+num%702//26) + chr(96+num%26)
    #位数为5
    if num <= 12356630:
        if num % 475254 == 0:
            return chr(96+num//475254-1) + chr(122) + chr(122) + chr(122) + chr(122)
        elif num % 18278 == 0:
            return chr(96+num//475254)

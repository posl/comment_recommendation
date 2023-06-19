def getChar(num):
    if num <= 26:
        return chr(num+96)
    elif num <= 702:
        num -= 26
        num -= 1
        return chr(num//26+97)+chr(num%26+97)
    elif num <= 18278:
        num -= 702
        num -= 1
        return chr(num//676+97)+chr(num%676//26+97)+chr(num%26+97)
    elif num <= 475254:
        num -= 18278
        num -= 1
        return chr(num//17576+97)+chr(num%17576//676+97)+chr(num%676//26+97)+chr(num%26+97)
    else:
        num -= 475254
        num -= 1
        return chr(num//17576+97)+chr(num%17576//676+97)+chr(num%676//26+97)+chr(num%26+97)
num = int(input())
print(getChar(num))

def get_name(num):
    if num <= 26:
        return chr(num+96)
    elif num <= 702:
        num -= 26
        return get_name(num//26)+get_name(num%26)
    elif num <= 18278:
        num -= 702
        return get_name(num//676)+get_name(num%676)
    elif num <= 475254:
        num -= 18278
        return get_name(num//17576)+get_name(num%17576)
    elif num <= 12356630:
        num -= 475254
        return get_name(num//456976)+get_name(num%456976)
    elif num <= 321272406:
        num -= 12356630
        return get_name(num//11881376)+get_name(num%11881376)
    elif num <= 8353082582:
        num -= 321272406
        return get_name(num//308915776)+get_name(num%308915776)
    elif num <= 217180147158:
        num -= 8353082582
        return get_name(num//8031810176)+get_name(num%8031810176)
    elif num <= 5669391237526:
        num -= 217180147158
        return get_name(num//19683)+get_name(num%19683)
    elif num <= 147808829414345:
        num -= 5669391237526
        return get_name(num//4826809)+get_name(num%4826809)
    elif num <= 3852657309928967:
        num -= 147808829414345
        return get_name(num//11881376)+get_name(num%11881376)
    elif num <= 100000000000000000:
        num -= 3852657309928967
        return get_name(num//308915776)+get_name(num%308915776)
    else:
        return "error"
num = int(input())
print(get_name(num))

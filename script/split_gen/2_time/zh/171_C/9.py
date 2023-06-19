def dog_name(n):
    if n <= 26:
        return chr(n+96)
    elif n <= 702:
        n -= 26
        return chr(n//26+96) + chr(n%26+96)
    elif n <= 18278:
        n -= 702
        return chr(n//676+96) + chr(n%676//26+96) + chr(n%26+96)
    elif n <= 475254:
        n -= 18278
        return chr(n//17576+96) + chr(n%17576//676+96) + chr(n%676//26+96) + chr(n%26+96)
    else:
        n -= 475254
        return chr(n//456976+96) + chr(n%456976//17576+96) + chr(n%17576//676+96) + chr(n%676//26+96) + chr(n%26+96)

def main():
    s = input()
    
    result = 0
    temp = 0
    for i in range(len(s)):
        if s[i] in ['A', 'T', 'C', 'G']:
            temp += 1
        else:
            temp = 0
        result = max(result, temp)
    
    print(result)

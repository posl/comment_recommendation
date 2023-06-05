def solution(s):
    if s[0]!="A":
        return "WA"
    if "C" not in s[2:-1]:
        return "WA"
    if s[-1]=="C":
        return "WA"
    if s[1:s.index("C")].islower() and s[s.index("C")+1:].islower():
        return "AC"
    return "WA"

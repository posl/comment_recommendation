def replacestr(s):
    if "na" not in s:
        return s
    else:
        return replacestr(s.replace("na","nya",1))

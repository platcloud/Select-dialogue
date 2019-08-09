import re
def trans(STR):
    words = STR.split()
    p1 = re.compile(r'[“](.*?？|.*?。|.*?！)[”]', re.S)
    taici = []
    for word in words:
        m = re.findall(p1, word)
        if m:
            taici.append(m)
    return taici

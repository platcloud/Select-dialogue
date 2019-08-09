import re
def trans(STR):
    p1 = re.compile(r'[“](.*?)[”]', re.S)
    p2=re.compile(r'(.*?？|.*?。|.*?！)',re.S)
    m = re.findall(p1, STR)
    taici=[]
    for i in m:
        m1=re.findall(p2,i)
        if m1:
            taici.append(i)
    return taici


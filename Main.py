def max1(haha, kaka):
    if len(haha) == 1: return haha[0] 
    maxx = haha[0]
    for i in range(1, len(haha)):
        if kaka[haha[i]] > kaka[maxx]:
            maxx = haha[i]
    return maxx 
def chartFix(haha):
    kaka = [1 for _ in range(len(haha))]
    for i in range(1,len(haha)):
        gay = []
        for j in range(0,i):
            if haha[j] < haha[i]:
                gay += [j]
        if len(gay) == 0: continue
        kaka[i] += kaka[max1(gay, kaka)]
    return len(haha) - max(kaka)

# words = []
# freq = FrequencyMap(Text, k)
# m = max(freq.values())



def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m
            words.append(key)
            words.sort()
    return words
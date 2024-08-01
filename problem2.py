def Indexlarni_topish(words, x):
    return [i for i, word in enumerate(words) if x in word]

words = ["abc","bcd","aaaa","cbc"]
x = "a"
output = Indexlarni_topish(words, x)
print(output)
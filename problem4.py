sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

eng_katta_suz = 0
index = []

for i in sentences:
    sikl = 0
    for j in i:
        if j == ' ':
            sikl += 1
    if sikl > eng_katta_suz:
        eng_katta_suz = sikl
        index = i

print(f"Eng uzun gap:   {index}\nuzunligi -> {eng_katta_suz+1}")

bank = [[1, 2, 3], [3, 2, 1, 3], [4, 5, 6]]

mijoz1, mijoz2, mijoz3 = [mijoz for mijoz in bank]

print("Mijoz1:", mijoz1)
print("Mijoz2:", mijoz2)
print("Mijoz3:", mijoz3)

summa1 = 0
for i in mijoz1:
    summa1 += i

summa2 = 0
for i in mijoz2:
    summa2 += i
    
summa3 = 0
for i in mijoz3:
    summa3 += i

if summa1 > summa2  and summa1 > summa3:
    print(f"Birinchi mijozni summasi eng katta -> {summa1}")
elif summa2 > summa1 and summa2 > summa3:
    print(f"Ikkinchi mijozni summasi eng katta -> {summa2}")
elif summa3 > summa1 and summa3 > summa2:
    print(f"Uchinchi mijozni summasi eng katta -> {summa3}")
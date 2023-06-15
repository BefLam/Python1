s = input().split()
counts = []
for phrase in s:
    vowels = 0
    for letter in phrase:
        if letter in 'aeiouyAEIOUY':
            vowels += 1
    counts.append(vowels)

if len(set(counts)) == 1:
    print("Парам пам-пам")
else:
    print("Пам парам")
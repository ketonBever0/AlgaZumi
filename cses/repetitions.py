txt = input()[:1_000_000]
txt += "yz"
n = len(txt)

longest = 0


for i in range(n):
    j = i + 1

    current = 0
    while j < n and txt[j] == txt[i]:
        current += 1
        i += 1
        # print("egyezik")
    else:
        if current > longest:
            longest = current

if longest == 0:
    longest += 1

print(longest )

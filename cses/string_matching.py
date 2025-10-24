limit = 1_000_000
txt = input()[:limit]
pattern = input()[:limit]

count = 0
pos = 0

while True:
    jump_pos = pos + 1
    if jump_pos > len(txt):
        break
    else:
        if txt[jump_pos] == pattern:
            count += 1
            pos += 1
            continue

    find_pos = txt.find(pattern, pos)
    if find_pos == -1:
        break
    pos = find_pos + 1
    count += 1
    # txt = txt[find_pos:]
    # print(txt[pos:])

print(count)
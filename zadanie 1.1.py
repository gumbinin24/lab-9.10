s = input()
res = ''
for i in range(0, len(s)):
    if s[i] in '0123456789':
        continue
    p = i + 1
    num = ''
    while (p < len(s)) and (s[p] in '0123456789'):
        num += s[p]
        p += 1
    num = int(num)
    res += s[i] * num
print(res)

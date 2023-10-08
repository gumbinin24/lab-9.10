def string_cnt(s: str):
    res = ""
    prev = s[0]
    counter = 1
    for i in range(1, len(s)):
        if s[i] == prev:
            counter += 1
        else:
            if counter == 1:
                res += prev
            else:
                res += prev + str(counter)
            prev = s[i]
            counter = 1
    if counter == 1:
        res += prev
    else:
        res += prev + str(counter)
    return res

print(string_cnt(input("Введите строку: \n")))
s = 'bobobqlpboobbobbobbflbobobbobobobobzobobuv'
i = 0
num_bobs = 0

while i < len(s)-2:
    if s[i] == 'b':
        i += 1
        if s[i] == 'o':
            i += 1
            if s[i] == 'b':
                num_bobs += 1
            else:
                i += 1
    else:
        i += 1
print num_bobs

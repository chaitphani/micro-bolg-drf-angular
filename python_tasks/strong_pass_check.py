def strong_password_checker(password):
    start, end, n, modify, count, c, l, need, remove, number, lower, upper = 0, 0, len(password), 0, [0] * 3, '', 0, 0, 0, True, True, True
    while end < n:
        c = password[end]
        if '0' <= c <= '9':
            number = False
        if 'a' <= c <= 'z':
            lower = False
        if 'A' <= c <= 'Z':
            upper = False
        while end < n and password[end] == c:
            end += 1
        l = end - start
        if l > 2:
            modify += l // 3
            count[l % 3] += 1
        start = end
    need = sum([number, lower, upper])
    if n < 6:
        print(max(6 - n, need))
    elif n <= 20:
        print(max(modify, need))


strong_password_checker('a')


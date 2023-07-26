table = [[0 for _ in range(8)] for _ in range(8)]

# Замінюємо непарні значення на 1
for i in range(len(table)):
    for j in range(len(table[i])):
        if ((i % 2 == 0 and j % 2 == 0) or (i % 2 == 1 and j % 2 == 1)):
            table[i][j] = "#"
        else:
            table[i][j] = ""

for row in table:
    print(row)

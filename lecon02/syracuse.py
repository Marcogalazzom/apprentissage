n = 27
etape = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    etape += 1
print(etape)

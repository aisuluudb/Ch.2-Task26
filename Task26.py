list = [2, 56, 7, 99, 456]
count_even = count_odd = 0

for numb in list:
    if numb %2 == 0:
        count_odd += 1
    else:
        count_even += 1
print ('Even numbers quantity:', count_even)
print ('Odd numbers quantity:', count_odd)
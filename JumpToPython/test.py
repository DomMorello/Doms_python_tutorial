marks = [90,38,58,79,98]

number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d pass" % number)
    else:
        print("%d fail" % number)

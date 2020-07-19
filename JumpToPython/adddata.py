f = open("new.txt", 'a')
for i in range(11, 20):
    data = "%d line added.\n" % i
    f.write(data)
f.close()
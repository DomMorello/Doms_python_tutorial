with open("test.txt", 'r') as f1:
    a = f1.read()
    if 'java' in a:
        a = a.replace('java','python')
        
with open("test.txt", 'w') as f2:
    f2.write(a)

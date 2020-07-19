# f = open("new1.txt", 'w')
# f.write("hello world\n")
# f.close()

# f = open("new1.txt", 'r')
# print(f.read())
# f.close()

with open("new1.txt", 'w') as f1:
    f1.write("foo bar")
with open("new1.txt", 'r') as f2:
    print(f2.read())
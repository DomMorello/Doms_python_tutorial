
def introduce(name, age, man=True):
    print("name is %s" % name)
    print("age is %d" % age)
    if man:
        print("male")
    else:
        print("female")

introduce("donglee", 28, False)
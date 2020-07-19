def get_avg(*args):
    ret = 0
    for i in args:
        ret += i
    return ret / len(args)

print(get_avg(3,5,6,2,243,34,5,2))
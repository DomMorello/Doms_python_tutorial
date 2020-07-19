# while 1:
#     a = input()
#     if not a: break
#     b = int(a)
#     if b % 2 == 0:
#         print("even")
#     else:
#         print("odd")

is_odd = lambda x: True if x % 2 == 1 else False
print(is_odd(4))
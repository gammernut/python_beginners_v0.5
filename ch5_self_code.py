# num = int(input('enter a number'))
# remainder = num % 2
#
#
# def even_odd():
#     if remainder == 0:
#         print('even')
#     else:
#         print('odd')
#
#
# even_odd()
# print(remainder)


num = None
remainder = None


def even_odd():
    if remainder == 0:
        print('even')
    else:
        print('odd')


while num != 0:
    num = int(input('enter a number'))
    remainder = num % 2
    even_odd()
    print(remainder)
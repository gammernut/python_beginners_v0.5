import datetime

right_now = datetime.datetime.now()

print(right_now)
me = 'jacob'
my_age = 24

user_name = input('whats your name?\n')
user_age = int(input('how old are you?\n'))


def difference(user_agge):
    if user_agge <= my_age:
        return my_age - user_agge
    else:
        return user_agge - my_age


diff = difference(user_age)

if user_age > my_age:
    print(f'hey {user_name} you are {diff} years older then {me}')
elif user_age == my_age:
    print(f'cool you and {me} are the same age')
else:
    print(f'hello {user_name} you are {diff} years younger then {me}')


# print(difference(user_age))
# print(user_name)
# print(user_age)
# print(diff)

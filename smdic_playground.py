
# Data structures
# 1. Dictionaries
# 2. Lists / arrays [1,1,7,11]
# 3. Sets


# Lists

lst = [1, 1, 11, 7]
print(lst)
lst.append(2)
print(lst)
lst.remove(11)
print(lst)
lst.sort()
print(lst)

# Sets:

st = {1, 1, 11, 7}
st.add(1)
st.add(1)
st.add(11)
print(st)

# Dictionaries

d = {
    'bob': 0,
    'sarah': 0,
    'defeated_by': {'paper', 'wolf'},
    'defeats': {'scissors', 'sponge'}
}

print(d['bob'])
d['bob'] += 1
print(d['bob'])
print(d)

d['jacob'] = 7

print(d)

print(f"you are defeated by {d['defeated_by']}")

# d['other']  # crash no suck thing as other at the moment gives keyerror: other
print(d.get('other'))
print(d.get('other', 42))

# x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
# print(x)

s = input()
t = input()

s = ''.join(sorted(s))
t = ''.join(sorted(t)[::-1])

print('Yes' if s < t else 'No')

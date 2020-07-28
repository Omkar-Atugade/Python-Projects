from random import choice

que = ['Why is the sky blue?:',
       'Why is there a face on the moon?:',
       'Where are all the dinosaures?:',
       'Why is the fire hot?:',
       'Why is Sun raises to East?:']

que = choice(que)

ans = input(que).strip().lower()

while ans != 'just because' :
    ans = input('Why?: ').strip().lower()

print('Ohhh....Okay!')

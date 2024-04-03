word = 'father'
new_word = ''
for r in word:
    new_word = r + new_word

if new_word == word: 
    print('palindrome')
else:
    print(f'word = {word} is not palindrome')
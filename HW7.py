word=''
prev_s=''
while True:
    s=input('input symbol and press enter: ') 
    if s!= prev_s:
        word = word+s
        prev_s = s
    else:
        print('stop duplictet symbol')
        break
print(f'your word is {word}') 







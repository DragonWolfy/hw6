a=1
while a>0:
    b=input('>Input a latin word: ')
    if b=='':
        print('>Error: No word was input')
        break
    else:
        if b.endswith ('ris'):
            with open("text.txt", "a", encoding="utf-8") as f:
                f.write(b)
                f.write('\n')
        elif b.endswith ('or'):
            with open("text.txt", "a", encoding="utf-8") as f:
                f.write(b)
                f.write('\n')
        elif b.endswith ('tur'):
            with open("text.txt", "a", encoding="utf-8") as f:
                f.write(b)
                f.write('\n')
        else:
            continue
    






words = []
while True:
    word = input(f"Digite uma palavra [ou enter para sair]")
    if not word:
        break
    final_word = ""    
    for letter in word:
        if letter.lower() in "aeiou":
            final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)
for word in words:
    print(word)    
    
            

            
            
    
    

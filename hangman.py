mistakes=0
MAINWORD="WORD" #replace this with your word
letters_guessed=[]
letters_left=["A","B","C","D","E","F","G","H","I",
              "J","K","L","M","N","O","P","Q","R",
              "S","T","U","V","W","X","Y","Z"]

word_list=[]
for i in range(0,len(MAINWORD)):
    word_list.append('__') 
    
real_word=[]
for i in range(0,len(MAINWORD)):
    if MAINWORD[i]!=" ":
        real_word.append(MAINWORD[i])
    else:
        real_word.append('__')

def split_long_list(given_list):
    big_lists=len(given_list)//9
    last_length=len(given_list)%9
    past_i=0
    for i in range (1,big_lists+1):
        print(given_list[past_i:past_i+9])
        past_i=i*9
    print(given_list[len(given_list)-last_length:len(given_list)])

def organize_letters():
    if letter in letters_left:
        letters_left.remove(letter)
        letters_guessed.append(letter)
    print("Letters guessed:")
    split_long_list(letters_guessed)
    print("Letters left:")
    split_long_list(letters_left)

def update_hangman():
    if mistakes==0:
        print("""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """)
    if mistakes==1:
        print("""
   _________
    |/   |      
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    H""")
    if mistakes==2:
        print("""
   _________       
    |/   |              
    |   (_)
    |                         
    |                       
    |                         
    |                          
    |___                       
    HA""")
    if mistakes==3:
        print("""
   ________               
    |/   |                   
    |   (_)                  
    |    |                     
    |    |                    
    |                           
    |                            
    |___                    
    HAN""")
    if mistakes==4:
        print("""
   _________             
    |/   |               
    |   (_)                   
    |   /|                     
    |    |                    
    |                        
    |                          
    |___                          
    HANG""")
    if mistakes==5:
        print("""
   _________              
    |/   |                     
    |   (_)                     
    |   /|\                    
    |    |                       
    |                             
    |                            
    |___                          
    HANGM""")
    if mistakes==6:
        print("""
   ________                   
    |/   |                         
    |   (_)                      
    |   /|\                             
    |    |                          
    |   /                            
    |                                  
    |___                              
    HANGMA""")
    if mistakes==7:
        print("""
   ________
    |/   |     
    |   (_)    
    |   /|\           
    |    |        
    |   / \        
    |               
    |___           
    HANGMAN""")

def ask_for_letter():
    letter=input("What letter would you like to guess? ")
    if letter in letters_guessed:
        print("You have already guessed this letter!")
        letter=input("What letter would you like to guess? ")
    return letter

def word_progress():
    for i in range(0,len(MAINWORD)):
        if letter==real_word[i]:
            word_list[i]=letter
    return word_list

def check_membership():
    if letter in letters_guessed:
        print("You already guessed this letter!")
        return True
    elif letter in real_word:
        print("This letter is in my word!")
        return True
    else:
        print("This letter is not in my word.")
        return False
    
def update_word_list():
    for i in range(0,len(real_word)):
        if real_word[i]==letter:
            word_list[i]=letter
    return word_list
        

print("Welcome to Hangman!")
print("Your job is to guess my word. My word has",len(MAINWORD),"letters.")
print("""
   _________
    |/        
    |              
    |                
    |                 
    |               
    |                   
    |___                 
    """)
print() 
print("My word...")
print(word_list)

def celebration_dance():
    for i in range(0,50):
        print("""
 (•_•)
<)   )╯
 /   \\""")
        print("""
  ( •_•)
 \(   (>
  /    \\""")
        print("""
 (•_•)
<)   )╯
 /    \\""")
    print()
 
# The actual game:

while word_list!=real_word:
    print()
    letter=ask_for_letter().upper()
    if check_membership()==False:
        mistakes+=1
        if mistakes<6:
            print("You have",7-mistakes,"chances left.")
            update_hangman()
        elif mistakes==7:
            print("You have 1 chance left.")
            update_hangman()
        else:
            update_hangman()
            print()
            print(real_word)
            print("HANGMAN! You lost. Better luck next time!")
            break
    else:
        update_word_list()
    print()
    print("My word...")
    print(word_list)
    word_list=word_progress()
    print()
    organize_letters()

if word_list==real_word:
    celebration_dance()
    print("Congratulations! You guessed it! Scroll up for a celebration dance.")

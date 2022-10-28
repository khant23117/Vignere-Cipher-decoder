from math import log2
frank =  "frank_encrypted.txt"
secret1 ="secret1_encrypted.txt"


def encrypt(text,key):
    alphabet = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    key = key.upper()
    encrypted =""
    for position in range (len(text)):
        text_character = alphabet.index (text[position])
        # print(key[position%len(key)])
        
        key_character = alphabet.index(key[position%len(key)])
        encrypted_character = (text_character + key_character) % len(alphabet)
        encrypted += alphabet[encrypted_character]
    return encrypted

def decrypt (text,key):
    '''Takes text and key and uses it to decrypt the text, using subtraction. Returns a decrypted string'''


    alphabet = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text = text.upper()
    key = key.upper()
    decrypted =""
    for position in range (len(text)):

        # find the text and key characters' index in our alphabet string
        text_character = alphabet.index(text[position])
        key_character = (alphabet.index(key[position%len(key)]))

        # find the index of the decrypted character using the length of the alphabet
        decrypted_character = (text_character - key_character) % len(alphabet)
        decrypted += alphabet[decrypted_character]
    return decrypted


def get_frequencies(file):
    '''takes a text and counts all the occurrences of each letter in that text, finds their relatice frequecncy and returns a 
    dictionary of frequencies'''

    
    alphabet = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    size = len(file)
    
    
    frequency = {}

    

    for letter in alphabet:
        count = file.count(letter)  
        if count != 0:
            # relative frequency
            frequency[letter] = count/size
                
    
    


    return frequency




def cross_entropy(freq1,freq2):
    '''finds the cross entropy between two frequency dictionaryes, uses log2 import and returns a numeric value'''


    # find all the letters that occur in both dictionaries
    overlap = list(freq2.keys())+list(freq1.keys())
    overlap = list(set(overlap))
   
    

    # total cross entropy variable
    total = 0.0
    
    # find the minimum frequency of each dictionary, incase there are missing objects in either
    min_freq1 = min(freq1.values())
    min_freq2 = min(freq2.values())
    
    
    
    for letter in overlap:
        # cross entropy calculations
        if letter not in list(freq1.keys()):
        

            
            freq1[letter]= min_freq1
            
            total = total - (freq1[letter] * log2(freq2[letter]))
            
        

        elif letter not in list(freq2.keys()):


            freq2[letter] = min_freq2
            
            total = total - (freq1[letter] * log2(freq2[letter]))
        
        else:
            total = total - (freq1[letter] * log2(freq2[letter]))
    return total
            
    


        
        
    # print(cross_entropy(freq1,freq1))




def guess_key(text):
    ''' # #initialiize master key list, to collect the required data
    #     #what is the required data?
    
    #         # the key, we find it by using the decrypt function on the encrypted file.
    #         # in the key argument of decrypt function, we run all the characters in the alphabet string
    #         # the result of the decrypt function is a character 
    #         # run get frequencies on the file we ran the decrypt function on
    #         # get the cross entropy of that dictionary with the english frequencies
    #         # the letter that gives us the smallest cross entropy is our target
    #         # repeat two more times for the other letters of the key

    # returns a string that contains the key of the encrypted file'''

    #open file and read -- checks out
    unencrypted = open( "frank.txt","r")
    unencrypted = unencrypted.read()
    alphabet = "\n !\"'(),-.0123456789:;?ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    english_frequencies = get_frequencies (unencrypted)

   
                
    


    # # cycle through all the letters in the alphabet, and put them in the key arg of decrypt
    key_size = 3
    
    key_final = ""
    for i in range (key_size):
        key_check = {}
        
        
        
        for letter in alphabet:
            # split the text into 3s starting with the first, then second then third and so on 
            
            decryption = decrypt(text[i::key_size],letter)
            
            
    
            decrypted_frequencies = get_frequencies(decryption)
           
            c_entropy = cross_entropy (english_frequencies,decrypted_frequencies)
        

            key_check [ letter] = c_entropy
        # print(key_check)

        key_check = dict ((value, _key) for _key,value in key_check.items())

        min_check = min(list(key_check.keys()))

        key_final+= key_check[min_check]
            
    # print(key_final)

    return (key_final)
            

            
def crack(file):
    '''uses the guess_key and decrypt functions to translate/decode an encrypted file. Takes file or string as an argument
    and returns a string'''
    
    # incase file needs to opened and read 

    if not isinstance(file,str):
        file = open(file,"r")
        file = file.read()
   
    key = guess_key(file)
    print(key)

    cracked = decrypt(file,key)
    return(cracked)






    





        

   
            
        

    

        
        
        








  

                                              

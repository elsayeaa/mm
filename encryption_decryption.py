
My_character_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', \
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', \
                    'y', 'z', ' ', '\n']                           # Intializing our own set of characters, so we don't  
                                                                   # need the ASCII code of spaces or new lines!

#---------------------------------------------------------------------------------------------------------------------------

def decoding(text, key):
    
    '''
    Decodes a message based on a certain key
    Parameters  :
                 text, the message to be decoded
                 key, the key of decoding
    Return Value:
                 None
    '''
    
    text = text.lower()                                            # to have all letters lower case
    key = key.lower() 
    key_shift = 0                                                  # Initializing a variable to represent the shifting of the encoded message

    character_position = 0                                         # Initializing a variable to represent the position of the character in the encoded message

    new_position = 0                                               # Initializing a variable to represent the position of the character
                                                                   # after substracting the shifting from the character

    i = 0                                                          # The counter through the key string elements

    decoded_message = ''

    decoded_character = ''

    maximum = len(key) - 1                                         # The maximum value at which the counter i should stop and start from beginning

    for character in text:

 
        if i > maximum:                                            # to start from beginning after reaching the last character of the key string

            i = 0

        if character in My_character_set:

            character_position = My_character_set.index(character) # to have the position between 0 and 27

            key_shift = My_character_set.index(key[i])             # to have the position between 0 and 27
            
            new_position = character_position - key_shift          # the desired position after decoding

            if new_position <= -1:                                 # To wrap up between 0 and 25 only
                new_position += 28
                decoded_character = My_character_set[new_position] # the new character  after decoding (+26 for wrapping up)
                decoded_message += decoded_character               # the character is added to the decoded message
                
            else:
                
                decoded_character = My_character_set[new_position] # the new character after decoding
                decoded_message += decoded_character               # adds the character after decoding to the decoded_message

        else:

            decoded_message += character                           # if the character wasn't between a or z

        i += 1                                                     # to go through the key letters
        
    print(decoded_message)
                
            
#---------------------------------------------------------------------------------------------------------------------------
                
def encoding(text, key):
    
    '''
    Encodes a message based on a certain key
    Parameters  :
                 text, the message to be encoded
                 key, the key of encoding
    Return Value:
                 None
    '''
    
    text = text.lower()                                            # lowering all text to work only with lowercase letters
    key = key.lower() 
    key_shift = 0                                                  # Initializing a variable to represent the shifting of the  message
    
    character_position = 0                                         # Initializing a variable to represent the position of the character in the message
    
    new_position = 0                                               # Initializing a variable to represent the position of the character
                                                                   # after substracting the shifting from the character
    
    i = 0                                                          # The counter through the key string elements
    
    encoded_message = ''                                           # The maximum value at which the counter i should stop and start from beginning
    
    encoded_character = ''
    
    maximum = len(key) -  1
    
    for character in text:
        
       
        
        if i > maximum:                                            # to start from beginning after reaching the last character of the key string

                i = 0

        if character in My_character_set:
            
            
            character_position = My_character_set.index(character) # to have the position between 0 and 25
            
            key_shift          = My_character_set.index(key[i])    # to have the position between 0 and 25
            
            
            new_position = character_position + key_shift          # the desired position to encode
            
            if new_position >= 28:                                 # To wrap up between 0 and 25 only
                new_position -= 28
                encoded_character = My_character_set[new_position] # the new character  after encoding (+26 for wrapping up)
                encoded_message += encoded_character               # the character is added to the decoded message
                    
            else:

                encoded_character = My_character_set[new_position] # the new character after encoding
                encoded_message += encoded_character               # adds the character after encoding to the encoded_message
            
        else:
            
            encoded_message += character
            
        i += 1
        
        
    
    print(encoded_message)
    
#---------------------------------------------------------------------------------------------------------------------------

def encipher_space(text, key, encode):
    
    '''
    Enciphers a certain text based on a given code
    Parameters  :
                 text, the string to be encoded
                 key, the key of encoding
                 encode is a boolean to perform either decoding or encoding
    Return Value:
                 Encoded, the encoded text
                 Decoded, the decoded text
    '''

    if encode == 'e':
        
        encoding(text, key)
        
    else:
        
        decoding(text, key)
        
#---------------------------------------------------------------------------------------------------------------------------
        
def readingfile(file_name):

    '''
    Reads a file and converts it into a text
    Parameters:
               file_name, the name of the file that we will work on
    Return Value:
                 text, the file as a string. 
    '''
    
    textFile = open(file_name, 'r', encoding ='utf-8')                      
    text = textFile.read()                                                # Assigns the text inside the file to a string variable
    text = text[:-1]                                                      # To eliminate the new line character
    textFile.close()

    return text



#---------------------------------------------------------------------------------------------------------------------------
  
def main():
    
    '''
    Excutes the program to perform encoding and decoding 
    Parameters  :
                 None
    Return Value:
                 None 
    '''
    
    encode = input('Would you like to (e)ncode or (d)ecode? ')           

    file_name = input('What is your filename? ')
    
    text = readingfile(file_name)
    
    key = input('What is the key? ')

    encipher_space(text,key, encode)

                                            

main()

import random
import string

def generate_password():

    print("-----Random Password Generator-----")

    while True:
        try:
            length_input= input("Enter the length of your password:") 
            length=int(length_input)

            if length <= 0:
                print("Length must be positive and greater than 0! Enter again")
                continue # restart the loop again

            break # go out from the loop and to task

        except ValueError:
            print("Enter numerical value, it's length.")

    
    #String Manipulation

    letters= string.ascii_letters
    numbers=string.digits
    punctuation=string.punctuation


    #make a combined list

    all_characters= letters+numbers+punctuation

    #random generate

    password_list=random.choices(all_characters,k=length)

    #join the picked numbers

    password="".join(password_list)

    #print the generated password


    print(f"Your Generated Password is : {password}")


#Generate only if run this script directly
if __name__ == "__main__" :
    generate_password()

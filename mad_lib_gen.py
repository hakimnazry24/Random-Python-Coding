'''
Mad Lib Generator
Written by: Hakim Nazri
First written: 29 August 2022

my name is ___ and i am __ years old. Today, I am going to share a story. When I was a _______, I love to _________. Everyday, I will ________ and make my parents ______.
Now, I do it as my career. The end ..

Structure:
1. main()
2. text()
    - this fx will receive list input and replace the missing part
    - at the end, will output the result
3. get_input()
    - get input from user
    - append it to list
    - return list back to text()
'''

def text(txt):
    story = """
        My name is {} and I am {}. Today I am going to share a story. When I was {}, I love to {c}. 
        Everyday, I will {} and make my parents {}. Now I do it as my career. The end... 
        """
    print(story.format(txt[0], txt[1], txt[2], txt[3], txt[4], txt[5]))

def get_input():
    txt_arr = []
    for i in range(6):
        ipt = input("Enter text for {" + str(i) + "}: ")
        txt_arr.append(ipt)
    print(txt_arr)
    return txt_arr

def main():
    print('''
    WELCOME TO MAD LIB GENERATOR!!
    Fill in for the following story

    My name is {0} and I am {1}. Today I am going to share a story. When I was {2}, I love to {3}. 
    Everyday, I will {4} and make my parents {5}. Now I do it as my career. The end...

    ''')
    
    text(get_input())

if __name__ == "__main__":
    main()
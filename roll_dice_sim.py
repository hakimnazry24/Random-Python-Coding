'''
Author : Hakim Nazri
Version written : 29 September 2022

Description:
- program that imitate dice rolling
- user can use dice repeatedly as long as they want
- ask user to roll again

Structure:
- main()

- rolling_dice()
# generate random number between 1 and 6
# return random number back go display_dice()

- display_dice()
# display graphic text of dice
'''
import random

def rolling_dice():
    return random.randint(1, 6)

def display_dice(dice_num):
    switcher = {
        1: '''
            ____________
            |          |
            |          |
            |     *    |
            |          |
            |__________|''',
        
        2: '''
            ____________
            |          |
            |          |
            |    **    |
            |          |
            |__________|''',

        3: '''
            ____________
            |          |
            |          |
            |   * * *  |
            |          |
            |__________|''',

        4: '''
            ____________
            |          |
            |   *  *   |
            |   *  *   |
            |          |
            |__________|''',

        5: '''
            ____________
            |          |
            |   *  *   |
            |     *    |
            |   *  *   |
            |__________|''',

        6: '''
            ____________
            |          |
            |  * * *   |
            |          |
            |  * * *   |
            |__________|''',
    }
    print(switcher[dice_num])

def main():
    print('DICE ROLLING SIMULATOR')
    while True:
        ipt = input("Roll dice (y/n): ")
        if ipt == 'y' or ipt == 'Y':
            display_dice(rolling_dice())
        elif ipt == 'n' or ipt == 'N':
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

'''
Author: Hakim Nazri
First written : 29 August 2022

Description:
- this is program called Email Slicer
- basically slide email address into username and domain of the email
- sliced email will be stored in txt file

Structure:
- main()

- slicer()
# function that slice the email
# get email input from user as arg
# will return back username and domain in a list

- fileIO()
# function that write returned input from slicer() to txt file'''

def slicer(email):
    sliced_email = email.split("@")
    return sliced_email

def fileIO(data):
    file = open("name-domain.txt", "a")
    for i in data:
        file.write(i)
        file.write("\t\t\t")
    file.write("\n")

def main():
    print("EMAIL SLICER\n")
    while True:
        ipt = input('''Enter email
    (type "exit" to close the program) : ''')

        if ipt == "exit":
            break
        fileIO(slicer(ipt))



if __name__ == "__main__":
    main()
is_email = False
at_sign = "@"
Username = 'waynemask@adventures.org'

for letter in Username:
    if letter == at_sign:
        is_email = True
        break
        
if is_email == True:
    print(Username)
else:
    Username += '@adventures.org'
    print(Username)
Username = input("Enter Email: ")
at_sign = "@"
User = ""
Subscription = "+" + input("Subscription Name: ") + '@gmail.com'
is_email = False

for letter in Username:
    if letter == at_sign:
        is_email = True
        
if is_email == True:
    User = Username.partition(at_sign)[0] + Subscription
    print(User)
    
else:
    Username += Subscription
    print(Username)
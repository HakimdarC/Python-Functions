def validatepw():
    print("Enter number for your Age")
    age = input()
    while True:
        if age.isdecimal():
            break
        print("Enter a valid age!!")

    while True:
        print("choose your password")
        pw = input()
        if pw.isalnum():
            break
        print("Weak password!!!")
        print("Enter both characters and numbers")
        
            

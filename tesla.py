def DriverAge(age = 0):
    age = input ("Enter your Age : ")
    if int(age) <18 :
        print ("Sorry,You are not eligible to drive .")
    elif int(age) ==18 :
        print("Congrats for your first drive .")
    else :
        print("Enjoy your drive .")
DriverAge()
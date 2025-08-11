class multipleProcess():
     def Subfields():
        print("Sub-fields in AI are:\nMachine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")
         
     def OddEven():
         num = int(input("Enter a number:"))
         print("Enter a number:", num)
         if(num%2==1):
             print(num, "is Odd Number")
         else:
             print(num, "is Even Number")

     def Eligible():
         gender=input("Your Gender:")
         print("Your Gender:", gender)
         age=int(input("Your Age:"))
         print("Your Age:", age)
         if(gender=="male" and age >= 21):
             print("ELIGIBLE")
         elif(gender=="female" and age >= 18):
             print("ELIGIBLE")
         else:
             print("NOT ELIGIBLE")

     def Percentage(s1,s2,s3,s4,s5):
         print("Subject1=",s1,"\nSubject2=",s2,"\nSubject3=",s3,"\nSubject4=",s4,"\nSubject5=",s5)
         total=s1+s2+s3+s4+s5
         print("Total:",total)
         percentage = (total / 500) * 100
         print("Percentage:", percentage)

     def triangle():
         height=int(input("Height:"))
         print("Height:", height)
         breadth=int(input("Breadth:"))
         print("breadth:", breadth)
         print("Area formula: (Height*Breadth)/2")
         area=(height*breadth)/2
         print("Area of Tirangle:", area)
         height1=int(input("Height1:"))
         print("Height1:", height1)
         height2=int(input("Height2:"))
         print("Height2:", height2)
         breadth=int(input("Breadth:"))
         print("Perimeter formula: Height1+Height2+Breadth")
         perimeter=height1+height2+breadth
         print("Perimeter of Triangle:", perimeter)
         
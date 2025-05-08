class SubfieldsInAI():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
class OddEven():
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==1):
            print(num,"Odd number")
        else:
            print(num,"is Even number")
class EligiblityForMarriage():
    def Eligible():
        gender=input("Your Gender(male/female):")
        age=int(input("your Age:"))
        if(gender =='male'):
            if(age>=21):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif (gender =='female'):
            if(age>=18):
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
class FindPercent():
    def percentage():
        subject1 = int(input("Enter marks for Subject1: "))
        subject2 = int(input("Enter marks for Subject2: "))
        subject3 = int(input("Enter marks for Subject3: "))
        subject4 = int(input("Enter marks for Subject4: "))
        subject5 = int(input("Enter marks for Subject5: "))
        total = subject1 + subject2 + subject3 + subject4 + subject5
        percentage = (total / 500) * 100
        print("Subject1=",subject1)
        print("Subject2=",subject2)
        print("Subject3=",subject3)
        print("Subject4=",subject4)
        print("Subject5=",subject5)
        print("Total : ",total)
        print("Percentage : ",percentage)  
class triangle:
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        Area_triangle = (Height*Breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",Area_triangle)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth = int(input("Breadth:"))
        Perimeter_triangle = Height1+Height2+Breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:",Perimeter_triangle)
    
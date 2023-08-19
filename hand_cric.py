import random
o=int(input("Number of overs to be play "))
t=input("Type your choice Head for H and Tail for T ")
n=['H','T']
r=random.choice(n)
if t==r:
    print("You won the Toss!")
    a=int(input("enter the choice batting(1) or fielding(0) "))
    if a==1:
        print("you choose batting")
        sum=0
        for i in range(0,o*6):
            x=int(input("enter the number for Batting "))
            if x<=6:
                z=[1,2,3,4,5,6]
                y=random.choice(z)
                if x!=y:
                    print(y)
                    sum+=x
                else:
                    print(y)
                    print("Wicket for Computer!!")
                    break
            else:
                print("enter number from 1 to 6 ")
                break
        print("your score is ",sum)   
        print("Now you need to bowl! ")
        diff=0
        for i in range(0,o*6):
            x=int(input("enter the number for bowling "))
            if x<=6:
                z=[1,2,3,4,5,6]
                y=random.choice(z)
                if x!=y:
                    print(y)
                    if diff<sum:
                        diff+=y
                    else:
                        break
                else:
                    print(y)
                    print("Wicket for You!!")
                    break
            else:
                print("enter number from 1 to 6 ")
                break
        print("your score is ",sum)
        print("Computer score is ",diff)
        if sum>diff:
            print("Congratulations!!!")
            print("You won the match")
        elif sum==diff:
            print("Match is tied ")
        else:
            print("Computer won the match ")
            print("Better Luck Next Time! ")
    else:
        print("you choose fielding ")
        diff=0
        for i in range(0,o*6):
            x=int(input("enter the number for Bowling "))
            if x<=6:
                z=[1,2,3,4,5,6]
                y=random.choice(z)
                if x!=y:
                    print(y)
                    diff+=y
                else:
                    print(y)
                    print("Wicket For You!!")
                    break
            else:
                print("enter number from 1 to 6 ")
                break
        print("Computer score is ",diff)
        print("You need to Bat!")
        sum=0
        for i in range(0,o*6):
            x=int(input("enter the number for batting "))
            if x<=6:
                z=[1,2,3,4,5,6]
                y=random.choice(z)
                if x!=y:
                    print(y)
                    if sum<diff:
                        sum+=x
                    else:
                        break
                else:
                    print(y)
                    print("Wicket For Computer!!")
                    break
            else:
                print("enter number from 1 to 6 ")
                break
        print("Your score is ",sum)
        print("Computer score is ",diff)
        if sum>diff:
            print("Congratulations!!!")
            print("You won the match")
        elif sum==diff:
            print("Match is tied ")
        else:
            print("Computer won the match ")
            print("Better Luck Next Time! ")
        
elif t!=r:
    print("Computer won the Toss!")
    a=random.randint(0,1)
    if a==1:
        print("Computer chose to batting")
        diff=0
        for i in range(0,o*6):
            x=int(input("enter the number for Bowling "))
            if x<=6:
                z=[1,2,3,4,5,6]
                y=random.choice(z)
                if x!=y:
                    print(y)
                    diff+=y
                else:
                    print(y)
                    print("Wicket for You!!!")
                    break
            else:
                print("enter number from 1 to 6 ")
                break
        print("Computer score is ",diff)
        print("You need to Bat!")
        sum=0
        for i in range(0,o*6):
            x=int(input("enter the number for Batting "))
            if x<=6:
                z=[1,2,3,4,5,6]
                y=random.choice(z)
                if x!=y:
                    print(y)
                    if sum<diff:
                        sum+=x
                    else:
                        break
                else:
                    print(y)
                    print("Wicket for Computer!!!")
                    break
            else:
                print("enter number from 1 to 6 ")
                break
        print("Your score is ",sum)
        print("Computer score is ",diff)
        if diff>sum:
            print("Computer won the match")
            print("Better Luck Next Time! ")  
        elif diff==sum:
            print("match Tied ")
        else:
            print("Congratulations!!")
            print("You won the match")
    else:
        print("Computer chose to fielding ")
        sum=0
        for i in range(0,o*6):
            x=int(input("enter the number for Batting "))
            if x<=6:
                z=[1,2,3,4,5,6]
                y=random.choice(z)
                if x!=y:
                    print(y)
                    sum+=x
                else:
                    print(y)
                    print("Wicket for Computer!!")
                    break
            else:
                print("enter number from 1 to 6 ")
                break
        print("Your score is ",sum)
        print("You need to bowl ")
        diff=0
        for i in range(0,o*6):
            x=int(input("enter the number for Bowling "))
            if x<=6:
                z=[1,2,3,4,5,6]
                y=random.choice(z)
                if x!=y:
                    print(y)
                    if diff<sum:
                        diff+=y
                    else:
                        break
                else:
                    print(y)
                    print("Wicket for You!!")
                    break
            else:
                print("enter number from 1 to 6 ")
                break
        print("Your score is ",sum)
        print("Computer score is ",diff)
        if diff>sum:
            print("Computer won the match ")
        elif diff==sum:
            print("Match tied ")
        else:
            print("Congratulations!!")
            print("You won the match ")
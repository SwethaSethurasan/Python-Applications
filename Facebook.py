import random
import sys
class Facebook:
    def __init__(self,username,pwd):
        self.username=username;
        self.pwd=pwd;
    def display(self):
        print(f"Welcome to Facebook,{self.username}")
class Post:
    def __init__(self,user):
        self.user=user;
    def like(self):
        like=random.randint(1,200)
        print(f"You have liked {self.user}'s post")
        like+=1
        print("Likes=",like)
    def comment(self):
        comment=[]
        comment1=input("Enter a comment:")
        comment.append(comment1)
        print(f"{self.user}'s Comments: {comment}")
    def shareto(self):
        Followers=["Anitha","subana","jevita","nivetha"]
        print("Your Followers:",Followers)
        share=input("Share To?=")
        print(f"You have sent a post to {share}")
username=input("Enter a username:")
pwd=input("Enter your password:")
fb=Facebook(username,pwd)
fb.display()
Followers=["Anitha","subana","jevita","nivetha"]
u1=random.choice(Followers)
P1=Post(u1)
print(f"You are into {u1}'s post")
while True:
    print('''1. like
2. Comment
3. Shareto
4. Exit''')

    match=int(input("Enter a choice 1-4:"))
    if(match == 1):
        P1.like();
    
    elif(match ==2):
        P1.comment()
    
    elif(match ==3):
        P1.shareto()
    
    elif(match ==4):
        sys.exit()
    else:
        print("Enter Valid choice")
        
        

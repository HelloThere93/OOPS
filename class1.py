class Dog:
    legs=4
    eyes=2
    hair="furry hair"
    tail=True
    paws=True
    def bark(self):
        print("BARK")
    
    def fetch(self,x):
        print("*Dog fetched the ball*",x)


husky=Dog()
labrador=Dog()
maltipoo=Dog()

print("Dog has: ",husky.hair)
print(labrador.eyes)
print(maltipoo.tail)

husky.bark()
maltipoo.fetch("maltipoo")
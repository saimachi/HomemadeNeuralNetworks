#Backpropogation doesn't have to be hard! 
#Let's conceptualize it with a simple arithmetic circuit!

def add_gate(a,b):
    return a+b

def multiply_gate(a,b):
    return a*b

#Defining our inputs to the circuit
a = 2
b = 3
c = 4

#The output
g = multiply_gate(a,b)
f = add_gate(g, c)

#What effect does changing c have on changing f? 
#Simply compute the partial derivative of f with respect to c!
#The addition gate add_gate(a,b) = a + b distributes the GRADIENT evenly.
#So, the gradient of c with respect to f is 1.0.
#Similarly, the gradient entering g (the multiplication gate) is also 1.0 with respect to f.

dfdc = 1.0
dfdg = 1.0

#Now we must consider the effects of a and b on f. To do this, we apply the chain rule.
#First, we must compute the LOCAL GRADIENT of a with respect to g.
#It is simply b--changing a by some amount correlates to an output increment by that amount times b. 
#Likewise, the local gradient of b with respect to g is a. 

dgda = b
dgdb = a

#Through the chain rule, the effects of a, b on c is thus:

dfda = dfdg * dgda
dfdb = dfdg * dgdb

print(dfda, dfdb)

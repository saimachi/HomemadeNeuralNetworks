import numpy as np
import torch

dev = torch.device('cuda:0')

def nonlin(x, deriv=False):
    if deriv:
        return x * (1 - x)
    return torch.exp(x) / (1 + torch.exp(x))


X = np.array([ [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
X = torch.as_tensor(X, dtype=torch.float, device=dev)

y = np.array([[0,0,1,1]]).T
y = torch.as_tensor(y, dtype=torch.float, device=dev)

syn0 = torch.randn((3,1), device=dev)

train_iterations = 10000

for iter in range(train_iterations):
    l0 = X #4x3 tensor
    l1 = nonlin(torch.mm(l0, syn0)) #4x3 * 3x1 = 4x1

    l1_error = y - l1 #4x1 
    l1_delta = l1_error * nonlin(l1, True) #4x1 by 4x1
    syn0 += torch.mm(l0.t(),l1_delta)

print(l1)

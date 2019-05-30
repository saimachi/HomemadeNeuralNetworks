import numpy as np
#Why is regularization important? 
#Regularization helps us achieve little loss on our validation data.
#In other words, regularization prevents overfitting. 
#Regularization penalizes model complexity.

#1. We have to minimize the loss of the model for a set of data plus the complexity of the model. 
#2. L2 = sum of squares of the weights
#3. Training optimization: Loss(Data|Model) + lambda * (w_1 ** 2 + w_2 ** 2 + ... + w_n ** 2)
lda = 1e-6
W = np.array([[0.2, 0.5, 5, 1, 0.25, 0.75]])

L2 = lda * np.sum(W**2, axis=1)
print(L2)

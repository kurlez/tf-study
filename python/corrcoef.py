# Correlation Coefficient

from numpy import *

featuremat = mat([[1, 2, 3, 4, 5, 6], [3, 4, 4, 1, 5, 6]])

mv1 = mean(featuremat[0])
mv2 = mean(featuremat[1])

dv1 = std(featuremat[0])
dv2 = std(featuremat[1])

corref = mean(multiply(featuremat[0]-mv1, featuremat[1]-mv2))/(dv1*dv2)
print corref

print corrcoef(featuremat)
import numpy as np
#Create arrays
a=np.array([1,2,3,4,5])
b=np.array([6,7,8,9,10])
#Basic operstions
print("Array a:",a)
print("Array b:",b)
print("Sum of arrays a and b",np.add(a,b))
print("Difference of arrays a and b",np.subtract(a,b))
print("Products of arrays a and b",np.multiply(a,b))
print("Divide of arrays a and b",np.divide(a,b))
print("Square root of array a",np.sqrt(a))
print("Exponential of array a",np.exp(a))
#Aggregation operations
print("Minimum value of array a",np.min(a))
print("Maximum value of array b",np.max(b))
print("mean of array a",np.mean(a))
print("Standard deviation of array b",np.std(b))
print("sum of all elements in array a",np.sum(a))
#Reshaping array
c=np.array([[1,2],[3,4],[5,6]])
print("array c:")
print(c)
print("Reshaped array c(2 rows,3 columns):",np.reshape(c,(2,3)))
#transposing arrays
d=np.array([[1,2,3],[4,5,6]])
print("array d:",d)
print("Transposed array d:\n",np.transpose(d))
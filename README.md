# sillysvm
A new implementation for a linear two-class Support Vector Machine

===

**Background**
I was reading the theory of how SVMs work and I thought "oh, I know how I'd do 
this!". Turns out how I thought it was done isn't how it is done. Before
diving into the math of how SVMs are actually implemented I wanted to try it
my way. And so SillySVM was born.

**Implementation**
Support vector machines work by finding the hyperplane that separates classes of
data with the largest margin between the plane and the data. The data points 
closest to the separating hyperplane are referred to as support vectors. In my 
implementation support vector of one class is the data point closest to the mean
of the other class. For now the implementation only supports two classes, but 
can be generalized to any number of dimensions. the hyperplane is now the plane
of vectors orthogonal to the line connecting the to support vectors and passing
through their midpoint.

**Upsides**
- This *probably* isn't less efficient than a normal SVM, which operates in
polynomial time. 

**Downsides**
Unsuprisingly this is a longer list.
- This SVM only supports two data classes
- There is only linear kernel support
- This SVM implementation can't account for outliers


'''takes a 2 dimenstional array that represents data points in a n dimensional 
space and labels s.t the ith label corresponds to the ith data points
returns a hyperplane consisting of a vector normal to a separating hyperplane
and a point it passes through'''
def train(data, labels):
    class0 = []
    class1 = []
    mean0 = []
    mean1 = []
    support_vector0 = [] 
    support_vector1 = []

    #calculate mean for each dimension while also populating class list
    for i in range(len(data)):
        if labels[i] == 0:
            class0.append(data[i])
        else:
            class1.append(data[i])
            
    mean0 = __calculate_mean(class0)
    mean1 = __calculate_mean(class1)
    support_vector0 = __find_supportvecs(class0, mean1)
    support_vector1 = __find_supportvecs(class1, mean0)
   
    midpoint = [((x+y)/2.0) for x,y in zip(support_vector0, support_vector1)]
    #this vector is normal to the separating hyperplane
    slope = [(x - y) for x,y in zip(support_vector0, support_vector1)] 
    hyperplane = (slope, midpoint)
    return hyperplane

'''evaluate the hyperplane (of the form ax + by + cz + ... = 0)
if the result is greater than 0 it lies above the plane and belongs to one class
and if not it belongs to the other
'''
def predict(data_point, hyperplane):
    value = sum([(hyperplane[0][x] * (data_point[x] - hyperplane[1][x])) for x \
            in range(len(data_point))])
    #TODO: account for higher values not corresponding to 'bigger' label
    if value > 0:
        return 0
    else:
        return 1

#finds the mean of a given class
def __calculate_mean(classN):
    mean = []
    for i in range(len(classN)):
        mean_i = 0.0
        count = 0.0
        for j in range(len(classN[i])):
                mean_i += classN[i][j]
                count += 1.0
        mean.append(mean_i/count)
    return mean

'''find the supportvectors used to form our separating hyperplane
this is done by finding the point in each class closest to the mean
of the other class'''
def __find_supportvecs(classN, mean):
    curr_min_dist = 10000000000000000 #TODO THIS IS BAD
    support_vector = []
    for i in range(len(classN)):
        distance = (sum([(x - y)**2.0 for x,y in zip(classN[i],mean)]))**0.5
        if distance < curr_min_dist:
            curr_min_dist = distance
            support_vector = classN[i]
    return support_vector

if __name__ == "__main__":
    #some test code
    data = [[1, 1] , [1, 2], [2, 1], [2, 2], [-1, -1], [-1, -2], [-2, -1], 
    [-2, -2]]
    labels  = [0, 0, 0, 0, 1, 1, 1, 1]
    hyperplane = train(data, labels)
    print(predict([-3, -3], hyperplane))

hyperplane = []
def train(data, labels):
    #find mean of each label
    #find support vectors
    #calculate hyperplane

    mean1 = []
    support_vector0 = [] 
    support_vector1 = []

    for i in range(len(data)):
        mean0_i = 0.0
        count0 = 0.0
        mean1_i = 0.0
        count1 = 0.0
        for j in range(len(data[i])):
        if labels[i] == 0:
            mean0_i += data[i][j]
            count0 += 1
        else:
            mean1_i += data[i][j]
            count1 +=1
        mean0.append(mean0_i/count0)
        mean1.append(mean1_i/count1)


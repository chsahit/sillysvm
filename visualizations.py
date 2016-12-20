import matplotlib.pyplot as plt
import sillysvm

data = [[1, 1], [1, 2], [2, 1], [2, 2], [-1, -1] ,[-1, -2], [-2, -1], [-2, -2]]
plt.plot([data[x][0] for x in range(len(data))], 
        [data[x][1] for x in range(len(data))], 'ro')
plt.axis([-4, 4, -4, 4])
hyperplane = sillysvm.train(data, [1, 1, 1, 1, 0, 0, 0, 0])
plt.plot(hyperplane[1][0], hyperplane[1][1], 'bo')
plt.show()

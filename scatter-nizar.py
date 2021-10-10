import numpy as np
import matplotlib.pyplot as plt


np.random.seed(19680801)
  
N = 30  
x = np.random.rand(N)
y = np.random.rand(N)

  
plt.scatter(x, y, c ="red")
  

plt.show()


import matplotlib.pyplot as plt

def geneGraf():
  labels = ['a','b','c','d']
  values = [100,200,300,400]
  
  fig, ax = plt.subplots()
  ax.bar(labels,values)
  plt.show()

if __name__ == '__main__':
  geneGraf()
import numpy as np

def calculate(list):

  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
	
  a=np.reshape(np.asarray(list), (3,3))
  calculations={
				'mean': [np.mean(a, axis=0).tolist(),np.mean(a, axis=1).tolist(),np.mean(a.flatten()).tolist()],
               'variance':[np.var(a, axis=0).tolist(),np.var(a, axis=1).tolist(),np.var(a.flatten()).tolist()],
               'standard deviation':[np.std(a, axis=0).tolist(),np.std(a, axis=1).tolist(),np.std(a.flatten()).tolist()],
               'max':[np.amax(a, axis=0).tolist(),np.amax(a, axis=1).tolist(),np.amax(a.flatten()).tolist()],
               'min':[np.amin(a, axis=0).tolist(),np.amin(a, axis=1).tolist(),np.amin(a.flatten()).tolist()],
               'sum':[np.sum(a, axis=0).tolist(),np.sum(a, axis=1).tolist(),np.sum(a.flatten()).tolist()]
			   }
  
  return calculations
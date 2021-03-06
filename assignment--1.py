

# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import bernoulli
import matplotlib.pyplot as plt

# probability data given from the question
# probabaility of item produced by operator A is defective
defpro_A = 0.01*0.5
# probabaility of item produced by operator B is defective
defpro_B = 0.05*0.3
# probabaility of item produced by operator C is defective
defpro_C = 0.07*0.2
defpro =  defpro_A + defpro_B + defpro_C
print("theoritical values")
print("probability of item produced by A is defective is ", defpro_A)
print("probability of item produced by B is defective is ", defpro_B)
print("probability of item produced by C is defective is ", defpro_C)
print("probability of item produced by either A orB orC is defective is", defpro)
print("\n\n")

trails=int(1e7)
#caluclating the bernoulli disturbutions for 10000000 trails 
defect_A_distirbution = bernoulli.rvs(defpro_A, size=trails)
defect_B_distirbution = bernoulli.rvs(defpro_B, size=trails)
defect_C_distirbution = bernoulli.rvs(defpro_C, size=trails)
#experimentally caluclated values 
exp_defpro_A = np.mean(defect_A_distirbution)
exp_defpro_B = np.mean(defect_B_distirbution)
exp_defpro_C = np.mean(defect_C_distirbution)
exp_defpro =  exp_defpro_A + exp_defpro_B + exp_defpro_C
print("experimental values")
print("probability of item produced by A is defective is ", exp_defpro_A)
print("probability of item produced by B is defective is ", exp_defpro_B)
print("probability of item produced by C is defective is ", exp_defpro_C)
print("probability of item produced by either A orB orC is defective is", exp_defpro)
print("\n\n")


#Taking these as our probability values and applying conditional probability Theorem we get the probability of a defective item coming from A
final_exp_prob = exp_defpro_A/(exp_defpro)
final_the_prob = defpro_A/(defpro) 
print(" Experimentally obtained probability is ", final_exp_prob)
print(" Theoretically obtained probability is ", final_the_prob)
print("difference in both measurements is ",final_exp_prob-final_the_prob)

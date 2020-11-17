#!/usr/bin/env python
# coding: utf-8

# # Programming Exercise 2: Constraint Satisfaction Problem

# <div class="alert alert-info">
#     <h3>Please read the following important information before starting with the programming exercise: </h3>
#     <p>In order to avoid problems with the relative file path we recommend to place the provided notebook and csp_programming_exercise.py file in the rootfolder of your <b>aima repository</b>.</p> 
#     <p>Do not use/install any additional packages, which are not provided in the requirements.txt of the  <b>aima repository</b>. </p>
#     <p>For modelling the constraint satisfaction problem you will have to define some variables. Do not change the names of variables that we provided you! Since we use these variables for an automatic evaluation, changing  variable names will result in failing the programming exercise. </p>
#     <p>Do not modify the example with the TWO + TWO = FOUR problem!</p>
#     <p>Do not modify the csp_programming_exercise.py!</p>
#     <p>After completing the exercise, download this jupyter notebook as *.py file (File &rarr; Download as 	&rarr; Python (.py)) </p>
#     <p>Before uploading this file together with your jupyter notebook to moodle, check if you can run <i>'python AI_Assignment2.py'</i> inside your anaconda environment in the root folder of your <b>aima repository</b>. If we are not able to run your submitted files in an environment with the packages provided by the requirements.txt of the <b>aima repository</b>, you will fail the programming exercise.</p>
#     
# </div>

# ## Initialization

# In[1]:


# Do not change this part.
from csp_programming_exercise import *
import sys, os
sys.path.append(os.path.realpath("aima"))


# ## Example for Solving a Constraint Satisfaction Problem

# In this exercise we are going to construct the Science Fair problem as a constraint satisfaction problem in Python using the csp library. The "TWO + TWO = FOUR" problem from the exercise (see Problem 3.4) will help us to understand how to model a constraint satisfaction problem with this library.
# 

# ### Constructing the Domains: TWO + TWO = FOUR

# We start with constructing the domains for our problem. As an example the domains for the TWO + TWO = FOUR- problem from the csp library are given. 

# In[2]:


# Do not change this part
# Here we form the domains for the variables: T, F, W, O, U, R, C1, C2 and C3
# Domains are formed using key-value pairs,
# where the key stands for the variable and the value is for the possible values
# set(range(1, 4)) is a short way of creating an array with numbers from 1 to 4
# set (range(1, 4)) == [1, 2, 3]
# Tip: Remember that you can construct arrays with any variable types

domains_TF = {'T': set(range(1, 10)),
           'F': set(range(1, 10)),
           'W': set(range(0, 10)),
           'O': set(range(0, 10)),
           'U': set(range(0, 10)),
           'R': set(range(0, 10)),
           'C1': set(range(0, 2)), 
           'C2': set(range(0, 2)), 
           'C3': set(range(0, 2))
}


# ### Constructing the Constraints: TWO + TWO = FOUR

# We continue with defining the constraints for our problem, the most important part of any constraint satisfaction problem. Let's take a look at the constraints for our "TWO + TWO = FOUR" problem to give you some insight about how to construct constraints with the csp library.

# In[3]:


# Do not change this part
# Here we define our constraints
# The constraint constructor of csp takes two arguments:
# 1. The variables that take part in the constraint
# 2. The constraint itself which is a function that takes the variables as arguments and returns true or false
# all_diff and eq are functions defined in csp 
# Like their name suggest all_diff returns true if every value is different
# and eq returns true if the two values are equal
# Tip: Take a look at the lambda operator in python https://www.w3schools.com/python/python_lambda.asp


constraint1_TF = Constraint(('T', 'F', 'W', 'O', 'U', 'R'), all_diff)
constraint2_TF = Constraint(('O', 'R', 'C1'), lambda o, r, c1: o + o == r + 10 * c1)
constraint3_TF = Constraint(('W', 'U', 'C1', 'C2'), lambda w, u, c1, c2: c1 + w + w == u + 10 * c2)
constraint4_TF = Constraint(('T', 'O', 'C2', 'C3'), lambda t, o, c2, c3: c2 + t + t == o + 10 * c3)
constraint5_TF = Constraint(('F', 'C3'), eq)


# ### Combine the constraints and set up the TWO + TWO = FOUR Problem

# In[4]:


# Do not change this part
# TWO + TWO = FOUR Problem
two_four_constraints = [constraint1_TF, constraint2_TF, constraint3_TF, constraint4_TF, constraint5_TF]
two_four = NaryCSP(domains_TF, two_four_constraints)


# ### Solve the TWO + TWO = FOUR Problem

# In[5]:


# Do not change this part
ac_search_solver(two_four)


# ## Programming Exercise Science Fair 

# ### Constructing the Domains: Science Fair

# In[6]:


# Define your domains here
#Solar_Powered_Car  'SPC'
#Potato_Battery  'PB'
#Baking_Powder_Volcano  'BPV'
#Our_Solar_System 'OSS'

domains_SF = {              
           'Bella': {'SPC','PB','BPV','OSS'},
           'Bethany': {'SPC','PB','BPV','OSS'},
           'Brian': {'SPC','PB','BPV','OSS'},
           'Brianna': {'SPC','PB','BPV','OSS'},
           'Ben': {'SPC','PB','BPV','OSS'},
           'Bill': {'SPC','PB','BPV','OSS'},
           'Bart': {'SPC','PB','BPV','OSS'}  
}


# ### Constructing the Constraints: Science Fair

# In[7]:


# Define your constraints here

constraint1_SF = Constraint(('Bella','Bethany','Brian','Brianna','Ben','Bill','Bart'),
                            lambda bella, bethany, brian, brianna, ben, bill, bart :
                            (bella != None) and (bethany != None) and (brian != None) and (brianna != None) 
                            and (ben != None) and (bill != None) and (bart != None))

constraint2_SF = Constraint(('Bella','Bethany','Brian','Brianna','Ben','Bill','Bart'),
                            lambda bella, bethany, brian, brianna, ben, bill, bart : 
                            (bella == bethany or bella == brian or bella == brianna or bella == ben or bella == bill or bella == bart) and 
                            (bethany == bella or bethany == brian or bethany == brianna or bethany == ben or bethany == bill or bethany == bart) and 
                            (brian == bella or brian == bethany or brian == brianna or brian == ben or brian == bill or brian == bart) and 
                            (brianna == bella or brianna == bethany or brianna == brian or brianna == ben or brianna == bill or brianna == bart) and 
                            (ben  == bella or ben == bethany or ben == brian or ben == brianna or ben == bill or ben == bart) and 
                            (bill == bella or bill == bethany or bill == brian or bill == brianna or bill == ben or bill == bart) and 
                            (bart == bella or bart == bethany or bart == brian or bart == brianna or bart == ben or bart == bill))

constraint3_SF = Constraint(('Bella','Bethany','Brian','Brianna','Ben','Bill','Bart'), 
                            lambda bella, bethany, brian, brianna, ben, bill, bart : 
                            ((bella == 'SPC') + (bethany == 'SPC') + (brian == 'SPC') + (brianna == 'SPC') + (ben == 'SPC') + (bill == 'SPC') + (bart == 'SPC')) >= 1 and                          
                            ((bella == 'PB') + (bethany == 'PB') + (brian == 'PB') + (brianna == 'PB') + (ben == 'PB') + (bill == 'PB') + (bart == 'PB')) >= 1 and   
                            ((bella == 'BPV') + (bethany == 'BPV') + (brian == 'BPV') + (brianna == 'BPV') + (ben == 'BPV') + (bill == 'BPV') + (bart == 'BPV')) >= 1 and            
                            ((bella == 'OSS') + (bethany == 'OSS') + (brian == 'OSS') + (brianna == 'OSS') + (ben == 'OSS') + (bill == 'OSS') + (bart == 'OSS')) >= 1)

constraint4_SF = Constraint(('Bella','Bethany','Brian','Brianna','Ben','Bill','Bart'),
                            lambda bella, bethany, brian, brianna, ben, bill, bart:
                            ((bella == 'SPC') + (bethany == 'SPC') + (brian == 'SPC') + (brianna == 'SPC') + (ben == 'SPC') + (bill == 'SPC') + (bart == 'SPC')) <= 4)

constraint5_SF = Constraint(('Bella','Bethany','Brian','Brianna','Ben','Bill','Bart'),
                             lambda bella, bethany, brian, brianna, ben, bill, bart:
                            ((bella == 'PB') + (bethany == 'PB') + (brian == 'PB') + (brianna == 'PB') + (ben == 'PB') + (bill == 'PB') + (bart == 'PB')) <= 3)

constraint6_SF = Constraint(('Bella','Bethany','Brian','Brianna','Ben','Bill','Bart'), 
                            lambda bella, bethany, brian, brianna, ben, bill, bart:
                            (((bella == 'BPV') + (bethany == 'BPV') + (brian == 'BPV') + (brianna == 'BPV') + (ben == 'BPV') + (bill == 'BPV') + (bart == 'BPV')) >= 3
                           and ((bella == 'BPV') + (bethany == 'BPV') + (brian == 'BPV') + (brianna == 'BPV') + (ben == 'BPV') + (bill == 'BPV') + (bart == 'BPV')) <= 5)
                           or ((bella == 'BPV') + (bethany == 'BPV') + (brian == 'BPV') + (brianna == 'BPV') + (ben == 'BPV') + (bill == 'BPV') + (bart == 'BPV')) == 0)

constraint7_SF = Constraint(('Bella','Bethany','Brian','Brianna','Ben','Bill','Bart'), 
                            lambda bella, bethany, brian, brianna, ben, bill, bart:
                            ((bella == 'OSS') + (bethany == 'OSS') + (brian == 'OSS') + (brianna == 'OSS') + (ben == 'OSS') + (bill == 'OSS') + (bart == 'OSS')) == 2 or
                            ((bella == 'OSS') + (bethany == 'OSS') + (brian == 'OSS') + (brianna == 'OSS') + (ben == 'OSS') + (bill == 'OSS') + (bart == 'OSS')) == 0)

constraint8_SF = Constraint(('Bart', 'Bethany'), eq)
constraint9_SF = Constraint(('Brian', 'Bill', 'Ben'), all_diff)
constraint10_SF = Constraint(('Bill', 'Brianna'), lambda bill, brianna : bill != 'BPV' and brianna != 'BPV')
constraint11_SF = Constraint(('Bella', 'Bill'), lambda bella, bill : bill == 'PB' and bella == 'PB')
constraint12_SF = Constraint(('Bella','Bethany','Brianna') ,
                             lambda bella, bethany, brianna : 
                             bella == bethany or bella == brianna)
constraint13_SF = Constraint(('Bella','Bethany','Brian','Brianna','Ben','Bill','Bart'),
                             lambda bella, bethany, brian, brianna, ben, bill, bart : 
                             ((bella == 'OSS') + (bethany == 'OSS') + (brian == 'OSS') + (brianna == 'OSS') + (ben == 'OSS') + (bill == 'OSS') + (bart == 'OSS')) == 0)
constraint14_SF = Constraint(('Brian', 'Brianna'), eq)


# ### Combine the constraints and set up the CSPs for the different problems

# <div class="alert alert-info">
#     <p>The variables csp_21, csp_22, .. are defined for setting up the CSPs for the corresponding problems. You have to use these variable names otherwise this will result in failing the programming exercise.</p> 
# </div>

# In[8]:


# Construct the Science Fair Problems

# Combine Constraints and set up the csp for Problem 2.1
# TODO: csp_21 = 

constraints_csp_21=[constraint1_SF,constraint2_SF,constraint4_SF,                   
                    constraint5_SF,constraint6_SF,constraint7_SF,
                    constraint8_SF,constraint9_SF,constraint10_SF,
                    constraint11_SF,constraint12_SF] 
csp_21 = NaryCSP(domains_SF, constraints_csp_21)

# Combine Constraints and set up the csp for Problem 2.2 
# TODO: csp_22 =

constraints_csp_22=[constraint1_SF,constraint3_SF,constraint4_SF,
                    constraint5_SF,constraint6_SF,constraint7_SF,
                    constraint8_SF,constraint9_SF,constraint10_SF,
                    constraint12_SF]
csp_22 = NaryCSP(domains_SF, constraints_csp_22)
# Combine Constraints and set up the csp for Problem 2.3
# TODO: csp_23 = 
constraints_csp_23=[constraint1_SF,constraint3_SF,constraint4_SF,
                    constraint5_SF,constraint6_SF,constraint7_SF,
                    constraint10_SF,constraint11_SF,constraint12_SF]
csp_23 = NaryCSP(domains_SF, constraints_csp_23)
# Combine Constraints and set up the csp for Problem 2.4
# TODO: csp_24 =
constraints_csp_24=[constraint1_SF,constraint2_SF,constraint4_SF,
                    constraint5_SF,constraint6_SF,constraint7_SF,
                    constraint10_SF,constraint11_SF,constraint12_SF,
                    constraint13_SF]
csp_24 = NaryCSP(domains_SF, constraints_csp_24)
# Combine Constraints and set up the csp for Problem 2.5
# TODO: csp_25 =
constraints_csp_25=[constraint1_SF,constraint2_SF,constraint4_SF,
                    constraint5_SF,constraint6_SF,constraint7_SF,
                    constraint8_SF,constraint9_SF,constraint10_SF,
                    constraint11_SF,constraint13_SF]
csp_25 = NaryCSP(domains_SF, constraints_csp_25)
# Combine Constraints and set up the csp for Problem 2.6
# TODO: csp_26 =
constraints_csp_26=[constraint1_SF,constraint2_SF,constraint4_SF,
                    constraint5_SF,constraint6_SF,constraint7_SF,
                    constraint10_SF,constraint11_SF,constraint12_SF,
                    constraint13_SF,constraint14_SF]
csp_26 = NaryCSP(domains_SF, constraints_csp_26)


# ### Solving the CSP

# <div class="alert alert-info">
#     <p>Do not change the following cell. If you can't execute the following cell, you may have renamed the variables defined by us.</p> 
# </div>

# In[9]:


ac_search_solver(csp_21)
ac_search_solver(csp_22)
ac_search_solver(csp_23)
ac_search_solver(csp_24)
ac_search_solver(csp_25)
ac_search_solver(csp_26)



# Algorithm - 1

ALGORITHM: Energy Allotment System

INPUTS:

- windmill_generation: a list of dictionaries with each dictionary representing a windmill and its generation in kwh for each slot
- consumer_consumption: a list of dictionaries with each dictionary representing a consumer and its consumption in kwh for each slot
- priority_weight_matrix: a list of dictionaries with each dictionary representing the priority weight of each consumer for each slot

OUTPUT:

- energy_allotment: a list of dictionaries with each dictionary representing the allotted energy in kwh for each consumer in each slot

PROCEDURE:
ITERATION 0:
1. Initialize a dictionary `energy_allotment` to store the allotted energy in kwh for each consumer in each slot
2. For each slot, do the following:
    a. Initialize a dictionary `slot_allotment` to store the allotted energy in kwh for each consumer in the current slot
    b. For each consumer, do the following:
        i. Find the windmills the consumer is associated with
        ii. Calculate the total generation of the windmills for the current slot
        iii. Allocate the energy for the current consumer by multiplying the generation by the priority weight for the consumer in the current slot, and the minimum of the allocated energy and the consumer's consumption
        iv. Subtract the allocated energy from the total generation of the windmills
    c. Add the slot_allotment to the energy_allotment
3. Calculate the threshold by subtracting the total generation from the total consumption
4. For each windmill, do the following:
    a. Calculate the remaining energy for the current windmill
    b. If the remaining energy is greater than the threshold, redistribute the remaining energy to other consumers or windmills
    c. Repeat the above step until the remaining energy is less than the threshold or there are no more consumers or windmills to allocate the energy to
5. Return the energy_allotment

ITERATION 1: (CURRENT):

 1. User the one hot encoding for windmills to find relation between consumer and windmill
 2. Take the rate as parameter and create priority for each customer and windmill relation
 3. Multiple one hot encoding with priority to get final relation for allocation
 4. for each windmill
    1. For each slot
    2. Find the slot and customer priority
    3. sort the customer according to priorty and convert to list For each customer:
    4. if number of same priorities is 1:
       1. If available slot gen greater than 0:
          1. if generation greater than consumption:
             1. Allot consumption and update generation and consumption tables and add to allotment table
          2. if consumption greater than generation allot generation update consumption, generation and allotment tables
       2. Else:
          1. Break
    5. if number of same priorities greater than 1:
       1. If available slot gen greater than 0:
          1. if generation greater than consumption:
             1. Allot consumption and update generation/totalCustomers and consumption tables and add to allotment table
          2. if consumption greater than generation allot generation/totalCustomers update consumption, generation and allotment tables
       2. Else:
          1. Break
>>>>>>> 834faaa (init commit 2 iteration see readme for updates)

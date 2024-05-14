#Jupyter Notebook for PyPlate Recipe Design
#a) PyPlate Recipe for Cross-Coupling Reactions

#Python Code:
######
from pypolyplates import Plate, Well, Compound, Reaction

# Set random seed for reproducibility
seed = 1234

# Define reaction components (excluding Ai and Bi)
solvents = ["Toluene", "Glyme", "TBME", "Dichloroethane"]
ligands = ["XPhos", "SPhos", "dppf"]
pd_acetate = Compound("Pd(OAc)2", mw=333.2)  # Real MW
ligand_mw = 500  # Placeholder for ligand MW (assumed constant)

# Function to generate random molecular weights for Ai and Bi
def generate_mw(seed_val):
    import random
    random.seed(seed_val)
    return random.randint(100, 500)

# Define temperatures
temperatures = [60, 80]

# Create a 96-well plate object
plate = Plate(name="CrossCoupling_Screen")

# Loop through each reaction condition
for reaction_num in range(1, 13):
    # Generate random MWs for Ai and Bi
    ai_mw = generate_mw(seed + reaction_num)
    bi_mw = generate_mw(seed + 10 * reaction_num)

    # Define Ai and Bi compounds
    ai = Compound(f"A{reaction_num}", mw=ai_mw)
    bi = Compound(f"B{reaction_num}", mw=bi_mw)

    # Loop through all solvent and ligand combinations
    for solvent in solvents:
        for ligand in ligands:

            # Calculate required amounts
            ai_amount = 0.1  # Limiting reagent (mmol)
            bi_amount = 1.1 * (bi_mw / ai_mw) * ai_amount  # 1.1 equivalents of Bi
            pd_amount = 0.1 * ai_amount  # 10 mol% Pd(OAc)2
            ligand_amount = 0.15 * ai_amount * (ligand_mw / pd_acetate.mw)  # 15 mol% ligand

            # Create a well object
            well = Well(f"R{reaction_num}_{solvent}_{ligand}")
            plate.add_well(well)

            # Add compounds and their quantities to the well
            well.add_compound(ai, ai_amount)
            well.add_compound(bi, bi_amount)
            well.add_compound(pd_acetate, pd_amount)
            well.add_compound(ligand, ligand_amount)

            # Set solvent and reaction volume
            well.set_solvent(solvent)
            well.set_volume(200)

            # Define reaction conditions
            reaction = Reaction(temperature=temperatures[0])  # Initial temp (60°C)
            well.add_reaction(reaction)

            # Duplicate well for second temperature (80°C)
            duplicate_well = well.copy(f"{well.name}_80C")
            plate.add_well(duplicate_well)

            # Set reaction temperature for duplicate
            duplicate_well.reactions[0].temperature = temperatures[1]

# Visualize plate layout
plate.plot_layout(highlight="solvent")
plate.plot_layout(highlight="ligand")

##########


"""Explanation:
This code defines a PyPlate recipe for screening 12 cross-coupling reactions.
It uses a function with a fixed seed to generate random molecular weights for Ai and Bi for reproducibility.
Loops iterate through all combinations of solvents, ligands, and temperatures.
Within each loop, a well object is created and populated with compounds and their corresponding amounts based on stoichiometry and user-defined ratios.
The script defines separate reactions for each temperature (60°C and 80°C) within each well.
PyPlate visualization functions are used to illustrate the plate layout based on highlighted parameters (solvent and ligand in this case).
b) Modifying PyPlate for Non-Integer Equivalents

Here's how PyPlate could be modified to incorporate specifying non-integer equivalents:
API Changes:
Substance Class: Introduce a new attribute named tags to the Substance class. This attribute would be a list of strings representing tags associated with the substance.
Python Code:"""

class Substance:
  # Existing code...
  def __init__(self, name,
  
 ######################

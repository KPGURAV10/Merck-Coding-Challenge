#pip install pyplate

# Import necessary libraries
import numpy as np
import pyplate as pp

# Set the random seed for reproducibility
np.random.seed(42)

# Define the molecular weights of Ai and Bi (randomly generated)
molecular_weight_Ai = np.random.uniform(100, 200)  # Assuming molecular weight between 100 and 200 g/mol
molecular_weight_Bi = np.random.uniform(50, 150)   # Assuming molecular weight between 50 and 150 g/mol

# Define the experimental conditions
temperatures = [60, 80]  # °C
solvents = ['toluene', 'glyme', 'TBME', 'dichloroethane']
ligands = ['XPhos', 'SPhos', 'dppf']

# Define constants
limiting_reagent_amount = 0.1  # mmol
excess_Bi_equivalents = 1.1
palladium_percent = 10
ligand_percent = 15
total_reaction_volume = 200  # µL
well_plate_max_volume = 500  # µL

# Initialize PyPlate experiment
experiment = pp.Experiment(name="Cross-Coupling Screening")

# Loop over each reaction and set up the experiment
for i in range(1, 13):
    # Define Ai and Bi
    Ai = pp.Chemical(name=f"A{i}", molecular_weight=molecular_weight_Ai)
    Bi = pp.Chemical(name=f"B{i}", molecular_weight=molecular_weight_Bi)
    
    # Calculate amounts of Bi, Pd(OAc)2, and ligand
    amount_Bi = limiting_reagent_amount * excess_Bi_equivalents
    amount_palladium = total_reaction_volume * palladium_percent / 100
    amount_ligand = total_reaction_volume * ligand_percent / 100
    
    # Define the reaction
    reaction = pp.Reaction(inputs=[Ai, Bi], outputs=[f"C{i}"], conditions={
        'temperature': temperatures,
        'solvent': solvents,
        'ligand': ligands,
        'amounts': [amount_Bi, amount_palladium, amount_ligand]
    })
    
    # Add the reaction to the experiment
    experiment.add_reaction(reaction)

# Visualize the experimental layout
experiment.visualize_layout(well_plate_max_volume=well_plate_max_volume)

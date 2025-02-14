# Hugo Warscotte

import pyomo.environ as pyo

# Create a Pyomo model
model = pyo.ConcreteModel()

# Define model parameters
##########################################
############ CODE TO ADD HERE ############
##########################################

V_boat = 2e5 # [m³] Volume of a boat
LHV_NH3 = 18.5e6 # [J/kg] Lower Heating Value of NH3
rho_NH3 = 600 # [kg/m³] Density of NH3
rho_CH4 = 500 # [kg/m³] Density of CH4
LHV_CH4 = 50e6 # [J/kg] Lower Heating Value of CH4
losses_NH3 = 0.4 # [-] Losses of NH3   
losses_CH4 = 0.35 # [-] Losses of CH4
efficiency_NH3 = 0.25 # [tH2/tNH3] Efficiency of NH3
efficiency_CH4 = 0.3 # [tH2/tNH3] Efficiency of CH4
CH4_needs_CO2 = 2.5 # [tCO2/tCH4] CO2 needs for H2 production from CH4

# Define model variables
##########################################
############ CODE TO ADD HERE ############
##########################################

model.b_CH4 = pyo.Var(within=pyo.NonNegativeReals) # Number of CH4 boats
model.b_NH3 = pyo.Var(within=pyo.NonNegativeReals) # Number of NH3 boats

# Define the objective functions
##########################################
############ CODE TO ADD HERE ############
##########################################

model.obj = pyo.Objective(expr = V_boat * (rho_CH4 * efficiency_CH4 * model.b_CH4 + rho_NH3 * efficiency_NH3 * model.b_NH3), sense=pyo.maximize)

# Define the constraints
##########################################
############ CODE TO ADD HERE ############
##########################################

model.con1 = pyo.Constraint(expr = (model.b_CH4 + model.b_NH3 ) <= 100 ) # H2 production constraint
model.con2 = pyo.Constraint(expr = (V_boat*rho_CH4*model.b_CH4*LHV_CH4 / efficiency_CH4 + V_boat*rho_NH3*LHV_NH3*model.b_NH3/efficiency_NH3 <= 140e12 ) )
model.con3 = pyo.Constraint(expr = (V_boat*rho_CH4*model.b_CH4*CH4_needs_CO2 <= 14e9 ) ) # CO2 constraint
                    

# Specify the path towards your solver (gurobi) file
solver = pyo.SolverFactory("gurobi")
sol = solver.solve(model)

# Print here the number of CH4 boats and NH3 boats
##########################################
############ CODE TO ADD HERE ############
##########################################
print(model.b_CH4())
print(model.b_NH3())
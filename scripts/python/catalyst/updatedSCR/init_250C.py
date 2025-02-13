
import sys
sys.path.append('../..')
from catalyst.isothermal_monolith_catalysis import *

#Importing all reaction dictionaries
from rxns_v6 import *

# Create dict to iterate through
rxn_list = {"r5f": r5f,"r5r": r5r,"r6f": r6f,"r6r": r6r,"r7": r7,"r8": r8,"r9": r9,
            "r10": r10,"r11": r11,"r12": r12,"r13": r13,"r14": r14,
            "r15": r15,"r16": r16,"r17": r17,"r18": r18,"r19": r19,"r20": r20,
            "r21": r21,"r22": r22,"r23": r23,"r24": r24,"r25": r25,
            "r26": r26,"r27": r27,"r28": r28,"r29": r29,"r30": r30,"r31": r31,
            "r32": r32,"r33": r33,"r34": r34,"r35": r35,"r36": r36,
            "r37": r37,"r38": r38,"r39": r39}

T = 250 + 273.15
Tstr = "250C"
O2 = 0.002330029
H2O = 0.001174

# Apply transformation to kinetics for this temperature set
for rxn in rxn_list:
    k = arrhenius_rate_const(rxn_list[rxn]["parameters"]["A"], 0, rxn_list[rxn]["parameters"]["E"], T)
    rxn_list[rxn]["parameters"]["E"] = 0
    rxn_list[rxn]["parameters"]["A"] = k

# ========= create bulk of script ===========

# Read in the data (data is now a dictionary containing the data we want)
data = naively_read_data_file("inputfiles/SCR_all-ages_"+Tstr+".txt",factor=2)

time_list = time_point_selector(data["time"], data)

# Testing
sim = Isothermal_Monolith_Simulator()
sim.add_axial_dim(0,5)
sim.add_axial_dataset(5)       # Location of observations (in cm)

sim.add_temporal_dim(point_list=time_list)
sim.add_temporal_dataset(data["time"])   #Temporal observations (in min)

sim.add_age_set(["Unaged","2hr","4hr","8hr","16hr"])
sim.add_data_age_set(["Unaged","2hr","4hr","8hr","16hr"])  # Data observations can be a sub-set

sim.add_temperature_set([Tstr])
sim.add_data_temperature_set([Tstr])     # Data observations can be a sub-set

sim.add_gas_species(["NH3","H2O","O2","NO","NO2","N2O","N2"])
sim.add_data_gas_species(["NH3","NO","NO2","N2O"])    # Data observations can be a sub-set

sim.set_data_values_for("NH3","Unaged",Tstr,5,data["time"],data["NH3_Unaged"])
sim.set_data_values_for("NO","Unaged",Tstr,5,data["time"],data["NO_Unaged"])
sim.set_data_values_for("NO2","Unaged",Tstr,5,data["time"],data["NO2_Unaged"])
sim.set_data_values_for("N2O","Unaged",Tstr,5,data["time"],data["N2O_Unaged"])

sim.set_data_values_for("NH3","2hr",Tstr,5,data["time"],data["NH3_2hr"])
sim.set_data_values_for("NO","2hr",Tstr,5,data["time"],data["NO_2hr"])
sim.set_data_values_for("NO2","2hr",Tstr,5,data["time"],data["NO2_2hr"])
sim.set_data_values_for("N2O","2hr",Tstr,5,data["time"],data["N2O_2hr"])

sim.set_data_values_for("NH3","4hr",Tstr,5,data["time"],data["NH3_4hr"])
sim.set_data_values_for("NO","4hr",Tstr,5,data["time"],data["NO_4hr"])
sim.set_data_values_for("NO2","4hr",Tstr,5,data["time"],data["NO2_4hr"])
sim.set_data_values_for("N2O","4hr",Tstr,5,data["time"],data["N2O_4hr"])

sim.set_data_values_for("NH3","8hr",Tstr,5,data["time"],data["NH3_8hr"])
sim.set_data_values_for("NO","8hr",Tstr,5,data["time"],data["NO_8hr"])
sim.set_data_values_for("NO2","8hr",Tstr,5,data["time"],data["NO2_8hr"])
sim.set_data_values_for("N2O","8hr",Tstr,5,data["time"],data["N2O_8hr"])

sim.set_data_values_for("NH3","16hr",Tstr,5,data["time"],data["NH3_16hr"])
sim.set_data_values_for("NO","16hr",Tstr,5,data["time"],data["NO_16hr"])
sim.set_data_values_for("NO2","16hr",Tstr,5,data["time"],data["NO2_16hr"])
sim.set_data_values_for("N2O","16hr",Tstr,5,data["time"],data["N2O_16hr"])

#Clear up memory space after we don't need the dictionary anymore
data.clear()

sim.add_surface_species(["Z1CuOH-NH3",
                        "Z2Cu-NH3",
                        "Z2Cu-(NH3)2",
                        "ZNH4",
                        "Z1CuOH-H2O",
                        "Z2Cu-H2O",
                        "Z1CuOH-NH4NO3",
                        "Z2Cu-NH4NO3",
                        "ZH-NH4NO3"])
sim.add_surface_sites(["Z1CuOH","Z2Cu","ZH","CuO"])

sim.add_reactions({"r1": ReactionType.EquilibriumArrhenius,
                    "r2a": ReactionType.EquilibriumArrhenius,
                    "r2b": ReactionType.EquilibriumArrhenius,
                    "r3": ReactionType.EquilibriumArrhenius,
                    "r4a": ReactionType.EquilibriumArrhenius,
                    "r4b": ReactionType.EquilibriumArrhenius,

                    # NO Oxidation
                    "r5f": ReactionType.Arrhenius,
                    "r5r": ReactionType.Arrhenius,
                    "r6f": ReactionType.Arrhenius,
                    "r6r": ReactionType.Arrhenius,

                    #NH3 Oxidation to N2
                    "r7": ReactionType.Arrhenius,
                    "r8": ReactionType.Arrhenius,
                    "r9": ReactionType.Arrhenius,

                    #NH3 Oxidation to NO
                    "r10": ReactionType.Arrhenius,
                    "r11": ReactionType.Arrhenius,
                    "r12": ReactionType.Arrhenius,

                    #NO SCR
                    "r13": ReactionType.Arrhenius,
                    "r14": ReactionType.Arrhenius,
                    "r15": ReactionType.Arrhenius,
                    "r16": ReactionType.Arrhenius,
                    "r17": ReactionType.Arrhenius,

                    #N2O Formation from NO SCR
                    "r18": ReactionType.Arrhenius,
                    "r19": ReactionType.Arrhenius,
                    "r20": ReactionType.Arrhenius,

                    #NH4NO3 Formation
                    "r21": ReactionType.Arrhenius,
                    "r22": ReactionType.Arrhenius,
                    "r23": ReactionType.Arrhenius,
                    "r24": ReactionType.Arrhenius,

                    #NH4NO3 Fast SCR
                    "r25": ReactionType.Arrhenius,
                    "r26": ReactionType.Arrhenius,
                    "r27": ReactionType.Arrhenius,

                    #NH4NO3 NO2 SCR
                    "r28": ReactionType.Arrhenius,
                    "r29": ReactionType.Arrhenius,
                    "r30": ReactionType.Arrhenius,

                    #NH4NO3 N2O Formation
                    "r31": ReactionType.Arrhenius,
                    "r32": ReactionType.Arrhenius,
                    "r33": ReactionType.Arrhenius,

                    #CuO NH3 Oxidation @ High Temp
                    "r34": ReactionType.Arrhenius,
                    "r35": ReactionType.Arrhenius,
                    "r36": ReactionType.Arrhenius,

                    #N2O formation from NH3 oxidation
                    "r37": ReactionType.Arrhenius,
                    "r38": ReactionType.Arrhenius,
                    "r39": ReactionType.Arrhenius
                    })

sim.set_bulk_porosity(0.8)
sim.set_washcoat_porosity(0.4)
sim.set_reactor_radius(1)
sim.set_space_velocity_all_runs(1000)      #volumes/min
sim.set_cell_density(62)                   # 62 cells per cm^2 (~400 cpsi)

# Setting up site balances using dicts
s1_data = {"mol_occupancy": {"Z1CuOH-NH3": 1, "Z1CuOH-H2O": 1, "Z1CuOH-NH4NO3": 1}}
s2_data = {"mol_occupancy": {"Z2Cu-NH3": 1, "Z2Cu-(NH3)2": 1, "Z2Cu-H2O": 1, "Z2Cu-NH4NO3": 1}}
s3_data = {"mol_occupancy": {"ZNH4": 1, "ZH-NH4NO3": 1}}
CuO_data = {"mol_occupancy": {}}

sim.set_site_balance("Z1CuOH",s1_data)
sim.set_site_balance("Z2Cu",s2_data)
sim.set_site_balance("ZH",s3_data)
sim.set_site_balance("CuO",CuO_data)

sim.set_reaction_info("r1", r1_equ)
sim.set_reaction_info("r2a", r2a_equ)
sim.set_reaction_info("r2b", r2b_equ)
sim.set_reaction_info("r3", r3_equ)
sim.set_reaction_info("r4a", r4a_equ)
sim.set_reaction_info("r4b", r4b_equ)

sim.set_reaction_info("r5f", r5f)
sim.set_reaction_info("r5r", r5r)
sim.set_reaction_info("r6f", r6f)
sim.set_reaction_info("r6r", r6r)

sim.set_reaction_info("r7", r7)
sim.set_reaction_info("r8", r8)
sim.set_reaction_info("r9", r9)

sim.set_reaction_info("r10", r10)
sim.set_reaction_info("r11", r11)
sim.set_reaction_info("r12", r12)

sim.set_reaction_info("r13", r13)
sim.set_reaction_info("r14", r14)
sim.set_reaction_info("r15", r15)
sim.set_reaction_info("r16", r16)
sim.set_reaction_info("r17", r17)

sim.set_reaction_info("r18", r18)
sim.set_reaction_info("r19", r19)
sim.set_reaction_info("r20", r20)

sim.set_reaction_info("r21", r21)
sim.set_reaction_info("r22", r22)
sim.set_reaction_info("r23", r23)
sim.set_reaction_info("r24", r24)

sim.set_reaction_info("r25", r25)
sim.set_reaction_info("r26", r26)
sim.set_reaction_info("r27", r27)

sim.set_reaction_info("r28", r28)
sim.set_reaction_info("r29", r29)
sim.set_reaction_info("r30", r30)

sim.set_reaction_info("r31", r31)
sim.set_reaction_info("r32", r32)
sim.set_reaction_info("r33", r33)

sim.set_reaction_info("r34", r34)
sim.set_reaction_info("r35", r35)
sim.set_reaction_info("r36", r36)

sim.set_reaction_info("r37", r37)
sim.set_reaction_info("r38", r38)
sim.set_reaction_info("r39", r39)

# ----------------- Unaged Site Densities -----------
sim.set_site_density("Z1CuOH","Unaged",0.052619016)
sim.set_site_density("Z2Cu","Unaged",0.023125746)
sim.set_site_density("ZH","Unaged",0.01632+0.003233+0.006699)
sim.set_site_density("CuO","Unaged",0.001147378)

# ----------------- 2hr Site Densities -----------
sim.set_site_density("Z1CuOH","2hr",0.051274815)
sim.set_site_density("Z2Cu","2hr",0.025820144)
sim.set_site_density("ZH","2hr",0.009147918+0.000423397+0.008572669)
sim.set_site_density("CuO","2hr",2.0144E-05)

# ----------------- 4hr Site Densities -----------
sim.set_site_density("Z1CuOH","4hr",0.049679956)
sim.set_site_density("Z2Cu","4hr",0.02692473)
sim.set_site_density("ZH","4hr",0.005127864+5.54458E-05+0.009298203)
sim.set_site_density("CuO","4hr",7.85352E-07)

# ----------------- 8hr Site Densities -----------
sim.set_site_density("Z1CuOH","8hr",0.04838926)
sim.set_site_density("Z2Cu","8hr",0.026648589)
sim.set_site_density("ZH","8hr",0.001611258+9.50848E-07+0.009687883)
sim.set_site_density("CuO","8hr",4.54455E-09)

# ----------------- 16hr Site Densities -----------
sim.set_site_density("Z1CuOH","16hr",0.050359742)
sim.set_site_density("Z2Cu","16hr",0.025179871)
sim.set_site_density("ZH","16hr",0.000159082+2.79637E-10+0.009755058)
sim.set_site_density("CuO","16hr",2.33028E-12)

# Setup all temperatures
sim.set_isothermal_temp("Unaged",Tstr,T)
sim.set_isothermal_temp("2hr",Tstr,T)
sim.set_isothermal_temp("4hr",Tstr,T)
sim.set_isothermal_temp("8hr",Tstr,T)
sim.set_isothermal_temp("16hr",Tstr,T)

# Build the constraints then discretize
sim.build_constraints()
sim.discretize_model(method=DiscretizationMethod.OrthogonalCollocation,
                    tstep=90,elems=5,colpoints=2)

# Initial conditions and Boundary Conditions should be set AFTER discretization

# ---------------- Unaged ICs ------------------
sim.set_const_IC("O2","Unaged",Tstr,O2)
sim.set_const_IC("H2O","Unaged",Tstr,H2O)
sim.set_const_IC("NH3","Unaged",Tstr,0)
sim.set_const_IC("NO","Unaged",Tstr,0)
sim.set_const_IC("NO2","Unaged",Tstr,0)
sim.set_const_IC("N2O","Unaged",Tstr,0)
sim.set_const_IC("N2","Unaged",Tstr,0.0184)

sim.set_const_IC("Z1CuOH-NH3","Unaged",Tstr,0)
sim.set_const_IC("Z2Cu-NH3","Unaged",Tstr,0)
sim.set_const_IC("Z2Cu-(NH3)2","Unaged",Tstr,0)
sim.set_const_IC("ZNH4","Unaged",Tstr,0)
sim.set_const_IC("Z1CuOH-H2O","Unaged",Tstr,0)
sim.set_const_IC("Z2Cu-H2O","Unaged",Tstr,0)
sim.set_const_IC("Z1CuOH-NH4NO3","Unaged",Tstr,0)
sim.set_const_IC("Z2Cu-NH4NO3","Unaged",Tstr,0)
sim.set_const_IC("ZH-NH4NO3","Unaged",Tstr,0)

# ---------------- 2hr ICs ------------------
sim.set_const_IC("O2","2hr",Tstr,O2)
sim.set_const_IC("H2O","2hr",Tstr,H2O)
sim.set_const_IC("NH3","2hr",Tstr,0)
sim.set_const_IC("NO","2hr",Tstr,0)
sim.set_const_IC("NO2","2hr",Tstr,0)
sim.set_const_IC("N2O","2hr",Tstr,0)
sim.set_const_IC("N2","2hr",Tstr,0.0184)

sim.set_const_IC("Z1CuOH-NH3","2hr",Tstr,0)
sim.set_const_IC("Z2Cu-NH3","2hr",Tstr,0)
sim.set_const_IC("Z2Cu-(NH3)2","2hr",Tstr,0)
sim.set_const_IC("ZNH4","2hr",Tstr,0)
sim.set_const_IC("Z1CuOH-H2O","2hr",Tstr,0)
sim.set_const_IC("Z2Cu-H2O","2hr",Tstr,0)
sim.set_const_IC("Z1CuOH-NH4NO3","2hr",Tstr,0)
sim.set_const_IC("Z2Cu-NH4NO3","2hr",Tstr,0)
sim.set_const_IC("ZH-NH4NO3","2hr",Tstr,0)

# ---------------- 4hr ICs ------------------
sim.set_const_IC("O2","4hr",Tstr,O2)
sim.set_const_IC("H2O","4hr",Tstr,H2O)
sim.set_const_IC("NH3","4hr",Tstr,0)
sim.set_const_IC("NO","4hr",Tstr,0)
sim.set_const_IC("NO2","4hr",Tstr,0)
sim.set_const_IC("N2O","4hr",Tstr,0)
sim.set_const_IC("N2","4hr",Tstr,0.0184)

sim.set_const_IC("Z1CuOH-NH3","4hr",Tstr,0)
sim.set_const_IC("Z2Cu-NH3","4hr",Tstr,0)
sim.set_const_IC("Z2Cu-(NH3)2","4hr",Tstr,0)
sim.set_const_IC("ZNH4","4hr",Tstr,0)
sim.set_const_IC("Z1CuOH-H2O","4hr",Tstr,0)
sim.set_const_IC("Z2Cu-H2O","4hr",Tstr,0)
sim.set_const_IC("Z1CuOH-NH4NO3","4hr",Tstr,0)
sim.set_const_IC("Z2Cu-NH4NO3","4hr",Tstr,0)
sim.set_const_IC("ZH-NH4NO3","4hr",Tstr,0)

# ---------------- 8hr ICs ------------------
sim.set_const_IC("O2","8hr",Tstr,O2)
sim.set_const_IC("H2O","8hr",Tstr,H2O)
sim.set_const_IC("NH3","8hr",Tstr,0)
sim.set_const_IC("NO","8hr",Tstr,0)
sim.set_const_IC("NO2","8hr",Tstr,0)
sim.set_const_IC("N2O","8hr",Tstr,0)
sim.set_const_IC("N2","8hr",Tstr,0.0184)

sim.set_const_IC("Z1CuOH-NH3","8hr",Tstr,0)
sim.set_const_IC("Z2Cu-NH3","8hr",Tstr,0)
sim.set_const_IC("Z2Cu-(NH3)2","8hr",Tstr,0)
sim.set_const_IC("ZNH4","8hr",Tstr,0)
sim.set_const_IC("Z1CuOH-H2O","8hr",Tstr,0)
sim.set_const_IC("Z2Cu-H2O","8hr",Tstr,0)
sim.set_const_IC("Z1CuOH-NH4NO3","8hr",Tstr,0)
sim.set_const_IC("Z2Cu-NH4NO3","8hr",Tstr,0)
sim.set_const_IC("ZH-NH4NO3","8hr",Tstr,0)

# ---------------- 16hr ICs ------------------
sim.set_const_IC("O2","16hr",Tstr,O2)
sim.set_const_IC("H2O","16hr",Tstr,H2O)
sim.set_const_IC("NH3","16hr",Tstr,0)
sim.set_const_IC("NO","16hr",Tstr,0)
sim.set_const_IC("NO2","16hr",Tstr,0)
sim.set_const_IC("N2O","16hr",Tstr,0)
sim.set_const_IC("N2","16hr",Tstr,0.0184)

sim.set_const_IC("Z1CuOH-NH3","16hr",Tstr,0)
sim.set_const_IC("Z2Cu-NH3","16hr",Tstr,0)
sim.set_const_IC("Z2Cu-(NH3)2","16hr",Tstr,0)
sim.set_const_IC("ZNH4","16hr",Tstr,0)
sim.set_const_IC("Z1CuOH-H2O","16hr",Tstr,0)
sim.set_const_IC("Z2Cu-H2O","16hr",Tstr,0)
sim.set_const_IC("Z1CuOH-NH4NO3","16hr",Tstr,0)
sim.set_const_IC("Z2Cu-NH4NO3","16hr",Tstr,0)
sim.set_const_IC("ZH-NH4NO3","16hr",Tstr,0)


#Read in data tuples to use as BCs
data_tup = naively_read_data_file("inputfiles/protocol_SCR_all-ages_"+Tstr+".txt",
                                    factor=1,dict_of_tuples=True)

# ---------------- Unaged BCs ------------------
sim.set_time_dependent_BC("O2","Unaged",Tstr,
                            time_value_pairs=data_tup["O2_Unaged"],
                            initial_value=O2)

sim.set_time_dependent_BC("H2O","Unaged",Tstr,
                            time_value_pairs=data_tup["H2O_Unaged"],
                            initial_value=H2O)

sim.set_time_dependent_BC("NH3","Unaged",Tstr,
                            time_value_pairs=data_tup["NH3_Unaged"],
                            initial_value=0)

sim.set_time_dependent_BC("NO","Unaged",Tstr,
                            time_value_pairs=data_tup["NO_Unaged"],
                            initial_value=0)

sim.set_time_dependent_BC("NO2","Unaged",Tstr,
                            time_value_pairs=data_tup["NO2_Unaged"],
                            initial_value=0)

sim.set_const_BC("N2O","Unaged",Tstr,0)

sim.set_const_BC("N2","Unaged",Tstr,0.0184)


# ---------------- 2hr BCs ------------------
sim.set_time_dependent_BC("O2","2hr",Tstr,
                            time_value_pairs=data_tup["O2_2hr"],
                            initial_value=O2)

sim.set_time_dependent_BC("H2O","2hr",Tstr,
                            time_value_pairs=data_tup["H2O_2hr"],
                            initial_value=H2O)

sim.set_time_dependent_BC("NH3","2hr",Tstr,
                            time_value_pairs=data_tup["NH3_2hr"],
                            initial_value=0)

sim.set_time_dependent_BC("NO","2hr",Tstr,
                            time_value_pairs=data_tup["NO_2hr"],
                            initial_value=0)

sim.set_time_dependent_BC("NO2","2hr",Tstr,
                            time_value_pairs=data_tup["NO2_2hr"],
                            initial_value=0)

sim.set_const_BC("N2O","2hr",Tstr,0)

sim.set_const_BC("N2","2hr",Tstr,0.0184)


# ---------------- 4hr BCs ------------------
sim.set_time_dependent_BC("O2","4hr",Tstr,
                            time_value_pairs=data_tup["O2_4hr"],
                            initial_value=O2)

sim.set_time_dependent_BC("H2O","4hr",Tstr,
                            time_value_pairs=data_tup["H2O_4hr"],
                            initial_value=H2O)

sim.set_time_dependent_BC("NH3","4hr",Tstr,
                            time_value_pairs=data_tup["NH3_4hr"],
                            initial_value=0)

sim.set_time_dependent_BC("NO","4hr",Tstr,
                            time_value_pairs=data_tup["NO_4hr"],
                            initial_value=0)

sim.set_time_dependent_BC("NO2","4hr",Tstr,
                            time_value_pairs=data_tup["NO2_4hr"],
                            initial_value=0)

sim.set_const_BC("N2O","4hr",Tstr,0)

sim.set_const_BC("N2","4hr",Tstr,0.0184)


# ---------------- 8hr BCs ------------------
sim.set_time_dependent_BC("O2","8hr",Tstr,
                            time_value_pairs=data_tup["O2_8hr"],
                            initial_value=O2)

sim.set_time_dependent_BC("H2O","8hr",Tstr,
                            time_value_pairs=data_tup["H2O_8hr"],
                            initial_value=H2O)

sim.set_time_dependent_BC("NH3","8hr",Tstr,
                            time_value_pairs=data_tup["NH3_8hr"],
                            initial_value=0)

sim.set_time_dependent_BC("NO","8hr",Tstr,
                            time_value_pairs=data_tup["NO_8hr"],
                            initial_value=0)

sim.set_time_dependent_BC("NO2","8hr",Tstr,
                            time_value_pairs=data_tup["NO2_8hr"],
                            initial_value=0)

sim.set_const_BC("N2O","8hr",Tstr,0)

sim.set_const_BC("N2","8hr",Tstr,0.0184)


# ---------------- 16hr BCs ------------------
sim.set_time_dependent_BC("O2","16hr",Tstr,
                            time_value_pairs=data_tup["O2_16hr"],
                            initial_value=O2)

sim.set_time_dependent_BC("H2O","16hr",Tstr,
                            time_value_pairs=data_tup["H2O_16hr"],
                            initial_value=H2O)

sim.set_time_dependent_BC("NH3","16hr",Tstr,
                            time_value_pairs=data_tup["NH3_16hr"],
                            initial_value=0)

sim.set_time_dependent_BC("NO","16hr",Tstr,
                            time_value_pairs=data_tup["NO_16hr"],
                            initial_value=0)

sim.set_time_dependent_BC("NO2","16hr",Tstr,
                            time_value_pairs=data_tup["NO2_16hr"],
                            initial_value=0)

sim.set_const_BC("N2O","16hr",Tstr,0)

sim.set_const_BC("N2","16hr",Tstr,0.0184)

data_tup.clear()


# Fix all reactions for simulation mode only
sim.fix_all_reactions()

#Customize the weight factors
sim.auto_select_all_weight_factors()

#Select specific weight factor windows based on observed data
sim.ignore_weight_factor("NH3","Unaged",Tstr,time_window=(212,213))
sim.ignore_weight_factor("NO","Unaged",Tstr,time_window=(212,213))
sim.ignore_weight_factor("NO2","Unaged",Tstr,time_window=(212,213))
sim.ignore_weight_factor("N2O","Unaged",Tstr,time_window=(212,213))

sim.ignore_weight_factor("NH3","2hr",Tstr,time_window=(186,212))
sim.ignore_weight_factor("NO","2hr",Tstr,time_window=(186,212))
sim.ignore_weight_factor("NO2","2hr",Tstr,time_window=(186,212))
sim.ignore_weight_factor("N2O","2hr",Tstr,time_window=(186,212))

sim.ignore_weight_factor("NH3","4hr",Tstr,time_window=(178,212))
sim.ignore_weight_factor("NO","4hr",Tstr,time_window=(178,212))
sim.ignore_weight_factor("NO2","4hr",Tstr,time_window=(178,212))
sim.ignore_weight_factor("N2O","4hr",Tstr,time_window=(178,212))

sim.ignore_weight_factor("NH3","8hr",Tstr,time_window=(168,212))
sim.ignore_weight_factor("NO","8hr",Tstr,time_window=(168,212))
sim.ignore_weight_factor("NO2","8hr",Tstr,time_window=(168,212))
sim.ignore_weight_factor("N2O","8hr",Tstr,time_window=(168,212))

sim.ignore_weight_factor("NH3","16hr",Tstr,time_window=(162,212))
sim.ignore_weight_factor("NO","16hr",Tstr,time_window=(162,212))
sim.ignore_weight_factor("NO2","16hr",Tstr,time_window=(162,212))
sim.ignore_weight_factor("N2O","16hr",Tstr,time_window=(162,212))


sim.initialize_auto_scaling()
sim.initialize_simulator()

sim.finalize_auto_scaling()
sim.run_solver()


sim.print_results_of_breakthrough(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "Unaged", Tstr, file_name="Unaged_SCR_"+Tstr+"_breakthrough.txt")
sim.print_results_of_location(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "Unaged", Tstr, 0, file_name="Unaged_SCR_"+Tstr+"_bypass.txt")
sim.print_results_of_integral_average(["Z1CuOH-NH3","Z2Cu-NH3","Z2Cu-(NH3)2","ZNH4",
                                        "Z1CuOH-NH4NO3", "Z2Cu-NH4NO3", "ZH-NH4NO3"],
                                        "Unaged", Tstr, file_name="Unaged_SCR_"+Tstr+"_average_ads.txt")

sim.print_results_of_breakthrough(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "2hr", Tstr, file_name="2hr_SCR_"+Tstr+"_breakthrough.txt")
sim.print_results_of_location(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "2hr", Tstr, 0, file_name="2hr_SCR_"+Tstr+"_bypass.txt")
sim.print_results_of_integral_average(["Z1CuOH-NH3","Z2Cu-NH3","Z2Cu-(NH3)2","ZNH4",
                                        "Z1CuOH-NH4NO3", "Z2Cu-NH4NO3", "ZH-NH4NO3"],
                                        "2hr", Tstr, file_name="2hr_SCR_"+Tstr+"_average_ads.txt")

sim.print_results_of_breakthrough(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "4hr", Tstr, file_name="4hr_SCR_"+Tstr+"_breakthrough.txt")
sim.print_results_of_location(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "4hr", Tstr, 0, file_name="4hr_SCR_"+Tstr+"_bypass.txt")
sim.print_results_of_integral_average(["Z1CuOH-NH3","Z2Cu-NH3","Z2Cu-(NH3)2","ZNH4",
                                        "Z1CuOH-NH4NO3", "Z2Cu-NH4NO3", "ZH-NH4NO3"],
                                        "4hr", Tstr, file_name="4hr_SCR_"+Tstr+"_average_ads.txt")

sim.print_results_of_breakthrough(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "8hr", Tstr, file_name="8hr_SCR_"+Tstr+"_breakthrough.txt")
sim.print_results_of_location(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "8hr", Tstr, 0, file_name="8hr_SCR_"+Tstr+"_bypass.txt")
sim.print_results_of_integral_average(["Z1CuOH-NH3","Z2Cu-NH3","Z2Cu-(NH3)2","ZNH4",
                                        "Z1CuOH-NH4NO3", "Z2Cu-NH4NO3", "ZH-NH4NO3"],
                                        "8hr", Tstr, file_name="8hr_SCR_"+Tstr+"_average_ads.txt")

sim.print_results_of_breakthrough(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "16hr", Tstr, file_name="16hr_SCR_"+Tstr+"_breakthrough.txt")
sim.print_results_of_location(["NH3","NO","NO2","N2O","O2","N2","H2O"],
                                        "16hr", Tstr, 0, file_name="16hr_SCR_"+Tstr+"_bypass.txt")
sim.print_results_of_integral_average(["Z1CuOH-NH3","Z2Cu-NH3","Z2Cu-(NH3)2","ZNH4",
                                        "Z1CuOH-NH4NO3", "Z2Cu-NH4NO3", "ZH-NH4NO3"],
                                        "16hr", Tstr, file_name="16hr_SCR_"+Tstr+"_average_ads.txt")

sim.print_kinetic_parameter_info(file_name=Tstr+"_opt_params.txt")
sim.save_model_state(file_name=Tstr+"_model.json")

sim.plot_vs_data("NH3", "Unaged", Tstr, 5, display_live=False)
sim.plot_vs_data("NH3", "2hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NH3", "4hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NH3", "8hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NH3", "16hr", Tstr, 5, display_live=False)

sim.plot_vs_data("NO", "Unaged", Tstr, 5, display_live=False)
sim.plot_vs_data("NO", "2hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NO", "4hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NO", "8hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NO", "16hr", Tstr, 5, display_live=False)

sim.plot_vs_data("NO2", "Unaged", Tstr, 5, display_live=False)
sim.plot_vs_data("NO2", "2hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NO2", "4hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NO2", "8hr", Tstr, 5, display_live=False)
sim.plot_vs_data("NO2", "16hr", Tstr, 5, display_live=False)

sim.plot_vs_data("N2O", "Unaged", Tstr, 5, display_live=False)
sim.plot_vs_data("N2O", "2hr", Tstr, 5, display_live=False)
sim.plot_vs_data("N2O", "4hr", Tstr, 5, display_live=False)
sim.plot_vs_data("N2O", "8hr", Tstr, 5, display_live=False)
sim.plot_vs_data("N2O", "16hr", Tstr, 5, display_live=False)

[Mesh]
  type = GeneratedMesh
  dim = 2
  nx = 1
  ny = 1
[]

[Variables]
#O2 concentration (used as a variable for moving through time)
  [./O2]
    order = FIRST
    family = MONOMIAL
    initial_condition = 7100 #ppm
  [../]
 
  [./CO]
    order = FIRST
    family = MONOMIAL
    initial_condition = 5272 #ppm
  [../]
 
  [./H2]
    order = FIRST
    family = MONOMIAL
    initial_condition = 1670 #ppm
  [../]
 
  [./HC]
    order = FIRST
    family = MONOMIAL
    initial_condition = 3000 #ppm
  [../]
 
#NOTE: CANNOT name a variable 'NO' because MOOSE interprets this as instructions and not a name
  [./NOx]
    order = FIRST
    family = MONOMIAL
    initial_condition = 1063 #ppm
  [../]
 
  [./N2O]
    order = FIRST
    family = MONOMIAL
    initial_condition = 0 #ppm
  [../]
 
  [./NH3]
    order = FIRST
    family = MONOMIAL
    initial_condition = 0 #ppm
  [../]

#Inhibition variables
  [./R1]
    order = FIRST
    family = MONOMIAL
    initial_condition = 1970100
    #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
  [./R2]
    order = FIRST
    family = MONOMIAL
    initial_condition = 34394
   #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
  [./R3]
    order = FIRST
    family = MONOMIAL
    initial_condition = 64790185
   #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
  [./R4]
    order = FIRST
    family = MONOMIAL
    initial_condition = 11773591
   #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
  [./R5]
    order = FIRST
    family = MONOMIAL
    initial_condition = 9999775
   #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
  [./R6]
    order = FIRST
    family = MONOMIAL
    initial_condition = 10305525
   #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
  [./R8]
    order = FIRST
    family = MONOMIAL
    initial_condition = 83232803
   #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
  [./R10]
    order = FIRST
    family = MONOMIAL
    initial_condition = 2531262
   #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
  [./R14]
    order = FIRST
    family = MONOMIAL
    initial_condition = 1.1E7
   #Need to provide a good initial condition for R1 (otherwise, convergence is poor)
  [../]
 
#Coupled non-linear temperature
  [./temp]
    order = FIRST
    family = MONOMIAL
    initial_condition = 393.15  #K
  [../]
 
[]
 
[AuxVariables]
  [./temp_ref]
    order = FIRST
    family = MONOMIAL
    initial_condition = 393.15  #K
  [../]
  [./H2O]
    order = FIRST
    family = MONOMIAL
    initial_condition = 133562 #ppm
  [../]
 
#Inlet concentrations
  [./N2O_in]
    order = FIRST
    family = MONOMIAL
    initial_condition = 0 #ppm
  [../]
 
  [./NO_in]
    order = FIRST
    family = MONOMIAL
    initial_condition = 1063 #ppm
  [../]
 
  [./NH3_in]
    order = FIRST
    family = MONOMIAL
    initial_condition = 0 #ppm
  [../]
 
  [./HC_in]
    order = FIRST
    family = MONOMIAL
    initial_condition = 3000 #ppm
  [../]
  
  [./CO_in]
    order = FIRST
    family = MONOMIAL
    initial_condition = 5272 #ppm
  [../]
 
  [./H2_in]
    order = FIRST
    family = MONOMIAL
    initial_condition = 1670 #ppm
  [../]

[]

[Kernels]
  [./O2_time]
    type = CoefTimeDerivative
    variable = O2
    Coefficient = 1
  [../]
#Time coeff = 0.4945 or -0.4945
# Mass Balances
[./CO_time]
   type = CoefTimeDerivative
   variable = CO
   Coefficient = 0.4945
 [../]
  [./CO_conv]
    type = ConstMassTransfer
    variable = CO
    coupled = CO_in
    transfer_rate = -12.454
  [../]
  [./r1_rxn_CO]
    type = InhibitedArrheniusReaction
    variable = CO
    this_variable = CO
    temperature = temp
 
#    forward_pre_exponential = 1406.8
#    forward_activation_energy = 6992.5
#    forward_inhibition = R1

    forward_pre_exponential = 548194281
    forward_activation_energy = 112698
    forward_inhibition = 1

    scale = 1.0
    reactants = 'CO O2'
    reactant_stoich = '1 1'
    products = ''
    product_stoich = ''
  [../]
 [./r4_rxn_CO]
   type = InhibitedArrheniusReaction
   variable = CO
   this_variable = CO
   temperature = temp

   forward_pre_exponential = 0.004163666
   forward_activation_energy = 1322.3
   forward_inhibition = R4

   scale = 1.0
   reactants = 'CO NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 [./r5_rxn_CO]
   type = InhibitedArrheniusReaction
   variable = CO
   this_variable = CO
   temperature = temp

   forward_pre_exponential = 9.2124E-28
   forward_activation_energy = -230072.82
   forward_inhibition = R5

   scale = 1.0
   reactants = 'CO NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 [./r8_rxn_CO]
   type = InhibitedArrheniusReaction
   variable = CO
   this_variable = CO
   temperature = temp

   forward_pre_exponential = 168478.9
   forward_activation_energy = 119042.9
   forward_inhibition = R8

 scale = 0
#scale = 2.5
   reactants = 'CO NOx H2O'
   reactant_stoich = '1 1 1'
   products = ''
   product_stoich = ''
 [../]
 
# Mass Balances
 [./H2_time]
    type = CoefTimeDerivative
    variable = H2
    Coefficient = 0.4945
  [../]
  [./H2_conv]
    type = ConstMassTransfer
    variable = H2
    coupled = H2_in
    transfer_rate = -12.454
  [../]
  [./r2_rxn_H2]
    type = InhibitedArrheniusReaction
    variable = H2
    this_variable = H2
    temperature = temp

    forward_pre_exponential = 0.039345
    forward_activation_energy = -13001.4
    forward_inhibition = R2

    scale = 1.0
    reactants = 'H2 O2'
    reactant_stoich = '1 1'
    products = ''
    product_stoich = ''
  [../]
 [./r6_rxn_H2]
   type = InhibitedArrheniusReaction
   variable = H2
   this_variable = H2
   temperature = temp

   forward_pre_exponential = 10010.63
   forward_activation_energy = 49385.3
   forward_inhibition = R6

 scale = 0
#scale = 2.5
   reactants = 'H2 NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 [./r14_rxn_H2]
   type = InhibitedArrheniusReaction
   variable = H2
   this_variable = H2
   temperature = temp

   forward_pre_exponential = 0.98
   forward_activation_energy = -1274.6
   forward_inhibition = R14

 scale = 0
#scale = 1.0
   reactants = 'H2 NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 
# Mass Balances
 [./HC_time]
    type = CoefTimeDerivative
    variable = HC
    Coefficient = 0.4945
  [../]
  [./HC_conv]
    type = ConstMassTransfer
    variable = HC
    coupled = HC_in
    transfer_rate = -12.454
  [../]
  [./r3_rxn_HC]
    type = InhibitedArrheniusReaction
    variable = HC
    this_variable = HC
    temperature = temp

    forward_pre_exponential = 1.772693
    forward_activation_energy = -10890.9
    forward_inhibition = R3

    scale = 1.0
    reactants = 'HC O2'
    reactant_stoich = '1 1'
    products = ''
    product_stoich = ''
  [../]
 [./r10_rxn_HC]
   type = InhibitedArrheniusReaction
   variable = HC
   this_variable = HC
   temperature = temp

   forward_pre_exponential = 2667984
   forward_activation_energy = 45483.9
#forward_inhibition = R10
 forward_inhibition = 2E6

#scale = 0
scale = 1.0
   reactants = 'HC NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 
# Mass Balances
 [./NO_time]
    type = CoefTimeDerivative
    variable = NOx
    Coefficient = 0.4945
  [../]
  [./NO_conv]
    type = ConstMassTransfer
    variable = NOx
    coupled = NO_in
    transfer_rate = -12.454
  [../]
  [./r4_rxn_NO]
    type = InhibitedArrheniusReaction
    variable = NOx
    this_variable = NOx
    temperature = temp

    forward_pre_exponential = 0.004163666
    forward_activation_energy = 1322.3
    forward_inhibition = R4

    scale = 1.0
    reactants = 'CO NOx'
    reactant_stoich = '1 1'
    products = ''
    product_stoich = ''
  [../]
 [./r5_rxn_NO]
   type = InhibitedArrheniusReaction
   variable = NOx
   this_variable = NOx
   temperature = temp

   forward_pre_exponential = 9.2124E-28
   forward_activation_energy = -230072.82
   forward_inhibition = R5

   scale = 2.0
   reactants = 'CO NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 [./r6_rxn_NO]
   type = InhibitedArrheniusReaction
   variable = NOx
   this_variable = NOx
   temperature = temp

   forward_pre_exponential = 10010.63
   forward_activation_energy = 49385.3
   forward_inhibition = R6

 scale = 0
#scale = 1.0
   reactants = 'H2 NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 [./r8_rxn_NO]
   type = InhibitedArrheniusReaction
   variable = NOx
   this_variable = NOx
   temperature = temp

   forward_pre_exponential = 168478.9
   forward_activation_energy = 119042.9
   forward_inhibition = R8

 scale = 0
#scale = 1.0
   reactants = 'CO NOx H2O'
   reactant_stoich = '1 1 1'
   products = ''
   product_stoich = ''
 [../]
 [./r10_rxn_NO]
   type = InhibitedArrheniusReaction
   variable = NOx
   this_variable = NOx
   temperature = temp

   forward_pre_exponential = 2667984
   forward_activation_energy = 45483.9
   forward_inhibition = R10

#scale = 0
scale = 18.0
   reactants = 'HC NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 [./r14_rxn_NO]
   type = InhibitedArrheniusReaction
   variable = NOx
   this_variable = NOx
   temperature = temp

   forward_pre_exponential = 0.98
   forward_activation_energy = -1274.6
   forward_inhibition = R14

 scale = 0
#scale = 2.0
   reactants = 'H2 NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 
# Mass Balances
 [./N2O_time]
    type = CoefTimeDerivative
    variable = N2O
    Coefficient = 0.4945
  [../]
  [./N2O_conv]
    type = ConstMassTransfer
    variable = N2O
    coupled = N2O_in
    transfer_rate = -12.454
  [../]
  [./r5_rxn_N2O]
    type = InhibitedArrheniusReaction
    variable = N2O
    this_variable = N2O
    temperature = temp

    forward_pre_exponential = 9.2124E-28
    forward_activation_energy = -230072.82
    forward_inhibition = R5

    scale = -1.0
    reactants = 'CO NOx'
    reactant_stoich = '1 1'
    products = ''
    product_stoich = ''
  [../]
 [./r14_rxn_N2O]
   type = InhibitedArrheniusReaction
   variable = N2O
   this_variable = N2O
   temperature = temp

   forward_pre_exponential = 0.98
   forward_activation_energy = -1274.6
   forward_inhibition = R14

 scale = 0
#scale = -1.0
   reactants = 'H2 NOx'
   reactant_stoich = '1 1'
   products = ''
   product_stoich = ''
 [../]
 
# Mass Balances
 [./NH3_time]
    type = CoefTimeDerivative
    variable = NH3
    Coefficient = 0.4945
  [../]
  [./NH3_conv]
    type = ConstMassTransfer
    variable = NH3
    coupled = NH3_in
    transfer_rate = -12.454
  [../]
  [./r6_rxn_NH3]
    type = InhibitedArrheniusReaction
    variable = NH3
    this_variable = NH3
    temperature = temp

    forward_pre_exponential = 10010.63
    forward_activation_energy = 49385.3
    forward_inhibition = R6

 scale = 0
#scale = -1.0
    reactants = 'H2 NOx'
    reactant_stoich = '1 1'
    products = ''
    product_stoich = ''
  [../]
 [./r8_rxn_NH3]
   type = InhibitedArrheniusReaction
   variable = NH3
   this_variable = NH3
   temperature = temp

   forward_pre_exponential = 168478.9
   forward_activation_energy = 119042.9
   forward_inhibition = R8

 scale = 0
#scale = -1.0
   reactants = 'CO NOx H2O'
   reactant_stoich = '1 1 1'
   products = ''
   product_stoich = ''
 [../]

# Inhibitions
  [./R1_eq]
    type = Reaction
    variable = R1
  [../]
  [./R1_inhib]
    type = PairedLangmuirInhibition
    variable = R1
    temperature = temp
 
    coupled_list = 'CO'
    pre_exponentials = '525.1'
    activation_energies = '16340.5'
 
    coupled_i_list = 'CO'
    coupled_j_list = 'NOx'
    binary_pre_exp = '1.43E-5'
    binary_energies = '-33931.9'
  [../]
 
# Inhibitions
  [./R2_eq]
    type = Reaction
    variable = R2
  [../]
  [./R2_inhib]
    type = PairedLangmuirInhibition
    variable = R2
    temperature = temp
 
    coupled_list = 'H2'
    pre_exponentials = '62.43'
    activation_energies = '23658.4'
 
    coupled_i_list = 'CO CO'
    coupled_j_list = 'NOx H2'
    binary_pre_exp = '7.44E-10 3.42E-95'
    binary_energies = '-50750.6 -690724'
  [../]
 
# Inhibitions
  [./R3_eq]
    type = Reaction
    variable = R3
  [../]
  [./R3_inhib]
    type = PairedLangmuirInhibition
    variable = R3
    temperature = temp

    coupled_list = 'HC'
    pre_exponentials = '1.52'
    activation_energies = '14130.3'

    coupled_i_list = 'CO HC'
    coupled_j_list = 'HC H2'
    binary_pre_exp = '1.82E-8 1.32E-6'
    binary_energies = '-62835.9 -39411.9'
  [../]
 
# Inhibitions
  [./R4_eq]
    type = Reaction
    variable = R4
  [../]
  [./R4_inhib]
    type = PairedLangmuirInhibition
    variable = R4
    temperature = temp

    coupled_list = 'H2'
    pre_exponentials = '1'
    activation_energies = '368551'

    coupled_i_list = 'CO NOx'
    coupled_j_list = 'NOx H2'
    binary_pre_exp = '0.991 1.65E-51'
    binary_energies = '1233280.7 -381364.44'
  [../]
 
# Inhibitions
  [./R5_eq]
    type = Reaction
    variable = R5
  [../]
  [./R5_inhib]
    type = PairedLangmuirInhibition
    variable = R5
    temperature = temp

    coupled_list = 'CO H2'
    pre_exponentials = '1.28E-5 2.16E18'
    activation_energies = '407703 219253'

    coupled_i_list = 'CO NOx'
    coupled_j_list = 'HC H2'
    binary_pre_exp = '6.65E-14 3.53E-30'
    binary_energies = '269603 -228342.8'
  [../]
 
# Inhibitions
  [./R6_eq]
    type = Reaction
    variable = R6
  [../]
  [./R6_inhib]
    type = PairedLangmuirInhibition
    variable = R6
    temperature = temp

    coupled_list = 'H2'
    pre_exponentials = '4.93E-14'
    activation_energies = '-122752'

    coupled_i_list = 'CO HC'
    coupled_j_list = 'H2 NOx'
    binary_pre_exp = '57.96 3.46E-10'
    binary_energies = '89900 -75282'
  [../]
 
# Inhibitions
  [./R8_eq]
    type = Reaction
    variable = R8
  [../]
  [./R8_inhib]
    type = PairedLangmuirInhibition
    variable = R8
    temperature = temp

    coupled_list = 'H2'
    pre_exponentials = '1.63E-44'
    activation_energies = '-365055'

    coupled_i_list = 'CO'
    coupled_j_list = 'NOx'
    binary_pre_exp = '142278'
    binary_energies = '102428'
  [../]
 
# Inhibitions
  [./R10_eq]
    type = Reaction
    variable = R10
  [../]
  [./R10_inhib]
    type = PairedLangmuirInhibition
    variable = R10
    temperature = temp

    coupled_list = 'HC'
    pre_exponentials = '30262'
    activation_energies = '62654'

    coupled_i_list = 'HC'
    coupled_j_list = 'NOx'
    binary_pre_exp = '0.19'
    binary_energies = '-5404'
  [../]
 
# Inhibitions
  [./R14_eq]
    type = Reaction
    variable = R14
  [../]
  [./R14_inhib]
    type = PairedLangmuirInhibition
    variable = R14
    temperature = temp

    coupled_list = ''
    pre_exponentials = ''
    activation_energies = ''

    coupled_i_list = 'CO HC'
    coupled_j_list = 'H2 NOx'
    binary_pre_exp = '4.78E-5 3.147E-10'
    binary_energies = '19.99 -76171'
  [../]
 
#NOTE: This kernel is used to set the temperature equal to a reference temperature at each time step
#      The residual for this kernel is k*(T - T_ref)  (with k = 1)
  [./temp_equ]
    type = ConstMassTransfer
    variable = temp
    coupled = temp_ref
  [../]
[]
 
[AuxKernels]
    [./temp_ramp]
        type = LinearChangeInTime
        variable = temp_ref
        start_time = 0
        end_time = 50
        end_value = 793.15
    # Execute always at initial, then at either timestep_begin or timestep_end
        execute_on = 'initial timestep_begin'
    [../]
[]

[BCs]

[]

[Postprocessors]
    [./O2]
        type = ElementAverageValue
        variable = O2
        execute_on = 'initial timestep_end'
    [../]
    [./CO]
        type = ElementAverageValue
        variable = CO
        execute_on = 'initial timestep_end'
    [../]
    [./H2]
        type = ElementAverageValue
        variable = H2
        execute_on = 'initial timestep_end'
    [../]
    [./HC]
        type = ElementAverageValue
        variable = HC
        execute_on = 'initial timestep_end'
    [../]
    [./NO]
        type = ElementAverageValue
        variable = NOx
        execute_on = 'initial timestep_end'
    [../]
    [./N2O]
        type = ElementAverageValue
        variable = N2O
        execute_on = 'initial timestep_end'
    [../]
    [./NH3]
        type = ElementAverageValue
        variable = NH3
        execute_on = 'initial timestep_end'
    [../]
    [./T]
        type = ElementAverageValue
        variable = temp
        execute_on = 'initial timestep_end'
    [../]
[]

[Preconditioning]
  [./SMP_PJFNK]
    type = SMP
    full = true
  [../]
[] #END Preconditioning

[Executioner]
  type = Transient
  scheme = implicit-euler
#NOTE: The NEWTON solver is much better for steady-state problems
  solve_type = newton
  petsc_options = '-snes_converged_reason'
  petsc_options_iname ='-ksp_type -ksp_gmres_restart -pc_type -sub_pc_type'
  petsc_options_value = 'gmres 300 asm lu'

  #NOTE: turning off line search can help converge for high Renolds number
  line_search = none
  nl_rel_tol = 1e-10
  nl_abs_tol = 1e-6
  nl_rel_step_tol = 1e-10
  nl_abs_step_tol = 1e-10
  nl_max_its = 20
  l_tol = 1e-6
  l_max_its = 300

  start_time = 0
  end_time = 50
  dtmax = 1

  [./TimeStepper]
     type = ConstantDT
     dt = 1
  [../]
[] #END Executioner

[Outputs]
  print_linear_residuals = true
  exodus = true
  csv = true
  interval = 1
[] #END Outputs



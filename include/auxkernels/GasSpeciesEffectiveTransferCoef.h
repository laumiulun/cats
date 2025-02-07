/*!
 *  \file GasSpeciesEffectiveTransferCoef.h
 *    \brief AuxKernel kernel to compute the effective mass transfer coefficient for a given gas species
 *    \details This file is responsible for calculating the mass transfer in m/s
 *
 *
 *  \author Austin Ladshaw
 *  \date 04/20/2020
 *  \copyright This kernel was designed and built at the Georgia Institute
 *             of Technology by Austin Ladshaw for PhD research in the area
 *             of adsorption and surface science and was developed for use
 *               by Idaho National Laboratory and Oak Ridge National Laboratory
 *               engineers and scientists. Portions Copyright (c) 2015, all
 *             rights reserved.
 *
 *               Austin Ladshaw does not claim any ownership or copyright to the
 *               MOOSE framework in which these kernels are constructed, only
 *               the kernels themselves. The MOOSE framework copyright is held
 *               by the Battelle Energy Alliance, LLC (c) 2010, all rights reserved.
 */

#pragma once

#include "GasPropertiesBase.h"

/// GasSpeciesEffectiveTransferCoef class object inherits from GasPropertiesBase object
/** This class object inherits from the GasPropertiesBase object in the MOOSE framework.
    All public and protected members of this class are required function overrides.
    The kernel interfaces the set of non-linear variables to the kinetic theory of gases.  */
class GasSpeciesEffectiveTransferCoef : public GasPropertiesBase
{
public:
    /// Required new syntax for InputParameters
    static InputParameters validParams();

    /// Required constructor for objects in MOOSE
    GasSpeciesEffectiveTransferCoef(const InputParameters & parameters);

protected:
    /// Required MOOSE function override
    virtual Real computeValue() override;

    unsigned int _index;            ///< Index of the gas species to which the diffusion belongs
    const VariableValue & _porosity;                ///< Variable for the particle/washcoat porosity

private:

};

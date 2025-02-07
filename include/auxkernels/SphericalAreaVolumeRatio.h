/*!
 *  \file SphericalAreaVolumeRatio.h
 *    \brief Auxillary kernel to calculate the area-to-volume ratio of spherical particles
 *    \details This file is responsible for calculating the area-to-volume ratio
 *            for spherical particles of a particular size. The purpose is to have
 *            these values automatically calculated for usage in the 'FilmMassTransfer'
 *            or similar mass or energy transfer functions.
 *
 *  \author Austin Ladshaw
 *  \date 09/14/2021
 *  \copyright This kernel was designed and built at Oak Ridge National
 *              Laboratory by Austin Ladshaw for research in catalyst
 *              performance for new vehicle technologies.
 *
 *               Austin Ladshaw does not claim any ownership or copyright to the
 *               MOOSE framework in which these kernels are constructed, only
 *               the kernels themselves. The MOOSE framework copyright is held
 *               by the Battelle Energy Alliance, LLC (c) 2010, all rights reserved.
 */

#pragma once

#include "AuxKernel.h"

/// SphericalAreaVolumeRatio class inherits from AuxKernel
class SphericalAreaVolumeRatio : public AuxKernel
{
public:
    /// Required new syntax for InputParameters
    static InputParameters validParams();

    /// Standard MOOSE public constructor
    SphericalAreaVolumeRatio(const InputParameters & parameters);

protected:
    /// Required MOOSE function override
    virtual Real computeValue() override;

private:
    Real _particle_diameter;        ///< Diameter of the particle for which the ratio is calculated (L)
    const VariableValue & _bulk_porosity;       ///< Ratio of channel volume to total volume
    bool _PerSolidsVolume;     ///< Boolean to determine if ratio to be calculated is per solid volume or per total volume

};

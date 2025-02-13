/*!
 *  \file InitialDaviesActivityCoeff.h
 *    \brief Initial Condition kernel for a Davies activity coefficient variable
 *    \details This file is responsible for calculation of the initial activity coefficient of an
 *            ion in solution based on the Davies model. This kernel couples a variable for
 *            ionic strength with some Davies model parameters to produce the activity
 *            coefficient for an ion of a specific valence.
 *
 *  \author Austin Ladshaw
 *  \date 02/09/2022
 *  \copyright This kernel was designed and built at Oak Ridge National
 *              Laboratory by Austin Ladshaw for research in electrochemical
 *              CO2 conversion.
 *
 *               Austin Ladshaw does not claim any ownership or copyright to the
 *               MOOSE framework in which these kernels are constructed, only
 *               the kernels themselves. The MOOSE framework copyright is held
 *               by the Battelle Energy Alliance, LLC (c) 2010, all rights reserved.
 */

#include "InitialDaviesActivityCoeff.h"

registerMooseObject("catsApp", InitialDaviesActivityCoeff);

InputParameters InitialDaviesActivityCoeff::validParams()
{
    InputParameters params = InitialCondition::validParams();
    params.addCoupledVar("ionic_strength",0,"Ionic strength variable for the domain (MUST be in M) [default=0 M]");
    params.addCoupledVar("temperature",298,"Temperature variable for the domain (MUST be in K) [default=298 K]");
    params.addParam< Real >("fitting_param",1.82E6,"The Davies model fitting parameter [default=1.82E6]");
    params.addParam< Real >("dielectric_const",78.325,"Dielectric constant for the media [default=78.325 == Water]");
    params.addParam< Real >("ion_valence",0,"Charge or valence of the ion in question [default=0]");
    return params;
}

InitialDaviesActivityCoeff::InitialDaviesActivityCoeff(const InputParameters & parameters)
: InitialCondition(parameters),
_ionic_strength(coupledValue("ionic_strength")),
_temp(coupledValue("temperature")),
_fitted_param(getParam<Real>("fitting_param")),
_dielec(getParam<Real>("dielectric_const")),
_charge(getParam<Real>("ion_valence"))
{

}

Real InitialDaviesActivityCoeff::value(const Point & /*p*/)
{
    Real _a = _fitted_param*std::pow(_dielec*_temp[_qp], -3.0/2.0);
    Real _I = 0.0;
    if (_ionic_strength[_qp] > 0.0)
      _I = _ionic_strength[_qp];
    Real _log_gama = -_a*_charge*_charge*( (std::sqrt(_I)/(1.0+std::sqrt(_I))) - 0.3*_I);
    return std::pow(10.0, _log_gama);
}

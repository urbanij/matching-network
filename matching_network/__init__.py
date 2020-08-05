# @date        : Fri Mar 27 10:11:01 CET 2020
# @author(s)   : Francesco Urbani
# @file        : 
# @descritpion : 
#                
# 


"""Matching network module"""


import quantiphy

__version__ = '0.0.2'


PI = 3.141592653589793

class ReactiveComponent:
    """Reactive component class
    
    =====
    Args:
        reactance
        
    
    =====
    Examples:
    
        >>> ReactiveComponent(1000, f=1e6)
        Inductor:
            X = 1 kΩ ⇔ B = -1 mS
            L = 159.15 uH (@ 1 MHz)

        >>> ReactiveComponent(0, f=12e6)
        wire:
            X = 0 Ω ⇔ B = -inf

    --------------------------------
    Z = jX [Ω]
    """
    def __init__(self, reactance, f=None):
        self._frequency = f
        self._reactance = quantiphy.Quantity(str(reactance) + 'Ω')
        self._component_type = "L" if reactance > 0 else "C" if reactance < 0 else "wire"
        
        if f != None: 
            assert f > 0

            self._frequency = quantiphy.Quantity(str(f) + 'Hz')
        
            if self._component_type == "L":
                inductor_val = (self._reactance/(2*PI*self._frequency)).real
                self._component_value = quantiphy.Quantity(str(inductor_val) + 'H')
            elif self._component_type == "C":
                capacitor_val = (-1/(2*PI*self._frequency*self._reactance)).real
                self._component_value = quantiphy.Quantity(str(capacitor_val) + 'F')
            else:
                self._component_value = 0
        else:
            self._component_value = None

    def __eq__(self, other):
        return  self._frequency == other._frequency and \
                self._reactance == other._reactance

    def get_freq(self):
        """Return frequency"""
        return self._frequency
    
    def get_susceptance(self):
        """Return equivalent susceptance value"""
        if self._reactance != 0:
            return quantiphy.Quantity(str(-1/self._reactance) + 'S')
        else:
            return -np.inf
    
    def __repr__(self, a=3):
        rv = "Inductor" if self._component_type == "L" else "Capacitor" if self._component_type == "C" else "wire"
        rv += ":\n\t"
        rv += f"X = {self._reactance} ⇔ B = {self.get_susceptance() }"
        rv += f"\n\t\033[1m{self._component_type}\033[0;0m = \033[1m{self._component_value}\033[0;0m  (@ {self._frequency})" if self._frequency != None and self._component_type!='wire' else ""
        return rv




class Solution:
    def __init__(self, config_type, shunt_elem: ReactiveComponent, series_elem: ReactiveComponent):
        
        assert shunt_elem.get_freq() == series_elem.get_freq()
        
        self._config_type = config_type
        self._shunt_elem = shunt_elem
        self._series_elem = series_elem

    def __eq__(self, other):
        return  self._config_type == other._config_type and \
                self._shunt_elem  == other._shunt_elem  and \
                self._series_elem == other._series_elem
    
    def __repr__(self):
        if self._config_type == "shunt-series":
            return f"{self._config_type}\n\tShunt {self._shunt_elem}\n\tSeries {self._series_elem}\n"
        else:
            return f"{self._config_type}\n\tSeries {self._series_elem}\n\tShunt {self._shunt_elem}\n"





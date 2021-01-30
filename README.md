<div align="right" style="text-align:right"><i><a href="https://urbanij.github.io/">Francesco Urbani</a></i></div>

### Index of Jupyter (IPython) Notebooks

|Title                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|
|<a href="https://github.com/urbanij/matching-network/blob/master/aux/L-section_matching_calculations.ipynb">L-section_matching_calculations</a>|
|<a href="https://github.com/urbanij/matching-network/blob/master/aux/calculations.ipynb">Calculations</a>|
|<a href="https://github.com/urbanij/matching-network/blob/master/aux/demo_matching_network.ipynb">Demo</a>|



---


[![Downloads](https://pepy.tech/badge/matching-network)](https://pepy.tech/project/matching-network)


Installation
============

```sh
pip install matching_network
```



Documentation
=============


```python
>>> import matching_network as mn
>>>
>>> impedance_you_have         = 90 + 32j # Ω
>>> impedance_you_want_to_have = 175      # Ω
>>>
>>> frequency                  = 900e6    # Hz
>>>
>>> mn.L_section_matching(impedance_you_have, impedance_you_want_to_have, frequency).match()
From (90+32j) Ω to 175 Ω

normalized starting impedance = (90+32j)Ω/175Ω = 0.51429+0.18286j

#solutions: 2

series-shunt
    Series Inductor:
    X = 55.464 Ω ⇔ B = -18.03 mS
    L = 9.8082 nH  (@ 900 MHz)
    Shunt Capacitor:
    X = -180.07 Ω ⇔ B = 5.5533 mS
    C = 982.04 fF  (@ 900 MHz)

series-shunt
    Series Capacitor:
    X = -119.46 Ω ⇔ B = 8.3707 mS
    C = 1.4803 pF  (@ 900 MHz)
    Shunt Inductor:
    X = 180.07 Ω ⇔ B = -5.5533 mS
    L = 31.844 nH  (@ 900 MHz)

>>>
```

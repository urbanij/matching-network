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



    pip install matching-network



Documentation
=============


```python
import matching_network.L_section as mn


impedance_you_have         = 90+32j  # Ω 
impedance_you_want_to_have = 175     # Ω

frequency                  = 900e6   # Hz

mn.L_section_matching(impedance_you_have, impedance_you_want_to_have, frequency).match()
```


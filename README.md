<div align="right" style="text-align:right"><i><a href="https://urbanij.github.io/">Francesco Urbani</a></i></div>

<!-- Index of Jupyter (IPython) Notebooks -->

|Title                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|
|<a href="https://github.com/urbanij/matching-network/blob/master/aux/L-section_matching_calculations.ipynb">L-section_matching_calculations</a>|
|<a href="https://github.com/urbanij/matching-network/blob/master/aux/calculations.ipynb">Calculations</a>                                      |
|<a href="https://github.com/urbanij/matching-network/blob/master/aux/demo_matching_network.ipynb">Demo</a>                                     |



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


Or, straight from the CLI:
```bash
$ python -c "import matching_network as mn; print(mn.L_section_matching(100, 20+43j, 1e9).match())"
```
```
From 100 Ω to (20+43j) Ω

normalized starting impedance = 100Ω / (20+43j)Ω = 0.88928-1.912j

#solutions: 4

shunt-series
	Shunt Inductor:
	X = 50 Ω ⇔ B = -20 mS
	L = 7.9577 nH  (@ 1 GHz)
	Series Inductor:
	X = 3 Ω ⇔ B = -333.33 mS
	L = 477.46 pH  (@ 1 GHz)
shunt-series
	Shunt Capacitor:
	X = -50 Ω ⇔ B = 20 mS
	C = 3.1831 pF  (@ 1 GHz)
	Series Inductor:
	X = 83 Ω ⇔ B = -12.048 mS
	L = 13.21 nH  (@ 1 GHz)
series-shunt
	Series Inductor:
	X = 35.285 Ω ⇔ B = -28.341 mS
	L = 5.6157 nH  (@ 1 GHz)
	Shunt Inductor:
	X = 62.571 Ω ⇔ B = -15.982 mS
	L = 9.9585 nH  (@ 1 GHz)
series-shunt
	Series Capacitor:
	X = -35.285 Ω ⇔ B = 28.341 mS
	C = 4.5106 pF  (@ 1 GHz)
	Shunt Inductor:
	X = 44.929 Ω ⇔ B = -22.257 mS
	L = 7.1507 nH  (@ 1 GHz)
```

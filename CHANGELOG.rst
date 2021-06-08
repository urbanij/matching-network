
Changelog
=========

0.0.0 (2020-03-27)
------------------

* First release on PyPI.


0.1.6 (2021-06-08)
------------------

* Added possibility to pass by conductance, in mS, when called from CLI.
  E.g.:
  $ matching_network --from "24.3+8.3j mS"  --to 1.1+9.3j

  From (36.85280111620006-12.587582274257635j) Ω to (1.1+9.3j) Ω

  normalized starting impedance = (36.85280111620006-12.587582274257635j)Ω / (1.1+9.3j)Ω = -0.87259-4.0659j

    #solutions: 4

    shunt-series
        Shunt Inductor:
        X = 6.4545 Ω ⇔ B = -154.93 mS
        Series Inductor:
        X = 2.6624 Ω ⇔ B = -375.6 mS
    [...]
    
=====
Usage
=====

To use Matching Network in a project::

    >>> import matching_network.L_section as mn

    >>> mn.L_section_matching(123,231,54).match()

    From 123 Ω to 231 Ω

    normalized starting impedance = 123Ω/231Ω = 0.53247

    #solutions: 2

    series-shunt
        Series Inductor:
        X = 115.26 Ω ⇔ B = -8.6763 mS
        L = 339.7 mH  (@ 54 Hz)
        Shunt Capacitor:
        X = -246.52 Ω ⇔ B = 4.0565 mS
        C = 11.956 uF  (@ 54 Hz)
    series-shunt
        Series Capacitor:
        X = -115.26 Ω ⇔ B = 8.6763 mS
        C = 25.572 uF  (@ 54 Hz)
        Shunt Inductor:
        X = 246.52 Ω ⇔ B = -4.0565 mS
        L = 726.57 mH  (@ 54 Hz)


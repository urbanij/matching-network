
[![Downloads](https://pepy.tech/badge/matching-network)](https://pepy.tech/project/matching-network)


Installation
============


::
    pip install matching-network



Documentation
=============


::
    import matching_network.L_section as mn


    impedance_you_have         = 90+32j  # Ω 
    impedance_you_want_to_have = 175     # Ω

    frequency                  = 900e6   # Hz

    mn.L_section_matching(impedance_you_have, impedance_you_want_to_have, frequency).match()

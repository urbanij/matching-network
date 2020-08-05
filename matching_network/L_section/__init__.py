
from .. import ReactiveComponent
from .. import Solution

class L_section_matching:
    """
    L section matching network
    
    ============
    args:
        input_impedance:
            the impedance you want to have.
            
        output_impedance:
            the impedance you want to transform the input impedance to.
    
    returns:
        a list of solutions (2 to 4 different results depending on 
        the point on the Smith Chart you start from)
        
    
    Examples:
            >>> mn1 = L_section_matching(input_impedance=102+8j, output_impedance=10, frequency=100e6)
            >>> mn1.match()
            >>> mn1
        
            From (102+8j) Ω to 10 Ω

            #solutions: 2

            shunt-series
                Shunt Inductor:
                X = 34.612 Ω ⇔ B = -28.891 mS
                L = 55.087 nH  (@ 100 MHz)
                Series Capacitor:
                X = -30.435 Ω ⇔ B = 32.857 mS
                C = 52.294 pF  (@ 100 MHz)
            shunt-series
                Shunt Capacitor:
                X = -32.873 Ω ⇔ B = 30.42 mS
                C = 48.415 pF  (@ 100 MHz)
                Series Inductor:
                X = 30.435 Ω ⇔ B = -32.857 mS
                L = 48.438 nH  (@ 100 MHz
    """
    def __init__(self, input_impedance, output_impedance, frequency=None):
        
        assert input_impedance.real >= 0 and output_impedance.real >= 0
        
        self._Z1 = input_impedance
        self._Z2 = output_impedance
        self._normalized_impedance = input_impedance/output_impedance
        
        self._frequency = frequency
        self._solutions = []
        
        self._input_reactance = ReactiveComponent(input_impedance.imag, frequency)
        
    def match(self):
        R1 = self._Z1.real
        X1 = self._Z1.imag
        R2 = self._Z2.real
        X2 = self._Z2.imag

        if R1*(R1 - R2) + X1**2 >= 0:
            """
            shunt - series configuration (down coversion)
            
                                          jXser
                                       +--------+
                      +-----------+----+        +----+
                      |           |    +--------+
                      |           |
                     +++         +++                                                   1
            Z1 =     | |         | | jXshu             Z2 = R2 + jX2 = jXser + -----------------
            R1 + jX1 | |         | |                                             1        1
                     +++         +++                                           ----- + --------
                      |           |                                            jXshu   R1 + jX1
                      |           |
                      +-----------+------------------+
            
            """

            Xshu_1 = (R1*X2 + R2*X1 - R1*(X2 - ((R2*(R1**2 - R2*R1 + X1**2))/R1)**(1/2)))/(R1 - R2)
            Xser_1 = X2 - ((R2*(R1**2 - R2*R1 + X1**2))/R1)**(1/2)

            Xshu_2 = (R1*X2 + R2*X1 - R1*(X2 + ((R2*(R1**2 - R2*R1 + X1**2))/R1)**(1/2)))/(R1 - R2)
            Xser_2 = X2 + ((R2*(R1**2 - R2*R1 + X1**2))/R1)**(1/2)
            
            sol1 = Solution(
                    config_type="shunt-series", 
                    shunt_elem=ReactiveComponent(Xshu_1, f=self._frequency),
                    series_elem=ReactiveComponent(Xser_1, f=self._frequency)
                )
            
            sol2 = Solution(
                    config_type="shunt-series", 
                    shunt_elem=ReactiveComponent(Xshu_2, f=self._frequency),
                    series_elem=ReactiveComponent(Xser_2, f=self._frequency)
                )

            self._solutions.append(sol1)
            if sol2 != sol1: # do not duplicate solutions
                self._solutions.append(sol2)
     

        if R2*(R2 - R1) + X2**2 >= 0:
            """ series - shunt configuration (up conversion)
            
                                jXser
                              +--------+
                      +-------+        +-----+--------------+
                      |       +--------+     |
                      |                      |
                     +++                    +++                                          1
            Z1 =     | |                    | | jXshu       Z2 = R2 + jX2 = -------------------------
            R1 + jX1 | |                    | |                                1            1
                     +++                    +++                              ----  + ----------------
                      |                      |                               jXshu   R1 + jX1 + jXser
                      |                      |
                      +----------------------+---------------+


            """

            Xshu_1 = (R1*X2 + (R1*R2*(R2**2 - R1*R2 + X2**2))**(1/2))/(R1 - R2)
            Xser_1 = -(R2*X1 - (R1*R2*(R2**2 - R1*R2 + X2**2))**(1/2))/R2

            Xshu_2 = (R1*X2 - (R1*R2*(R2**2 - R1*R2 + X2**2))**(1/2))/(R1 - R2)
            Xser_2 = -(R2*X1 + (R1*R2*(R2**2 - R1*R2 + X2**2))**(1/2))/R2
            
            sol1 = Solution(
                    config_type="series-shunt", 
                    shunt_elem=ReactiveComponent(Xshu_1, f=self._frequency),
                    series_elem=ReactiveComponent(Xser_1, f=self._frequency)
                )
            
            sol2 = Solution(
                    config_type="series-shunt",
                    shunt_elem=ReactiveComponent(Xshu_2, f=self._frequency),
                    series_elem=ReactiveComponent(Xser_2, f=self._frequency)
                )
            
            self._solutions.append(sol1)
            if sol2 != sol1: # do not duplicate solutions
                self._solutions.append(sol2)

        return self


    def get_solutions(self):
        rv = ""
        for sol in self._solutions:
            rv += f"{sol._shunt_elem._component_type}={sol._shunt_elem._component_value}, "
            rv += f"{sol._series_elem._component_type}={sol._series_elem._component_value}, "
        return rv
        
        
    def get_input_reactance(self):
        return self._input_reactance
    
    def plot(self):
        pass
        delta_f = 2000
        freq = np.linspace(self._frequency-delta_f/2, self._frequency+delta_f/2, 2000)
        for solution in self._solutions:
            print(solution)
            if solution._config_type=="shunt-series":
                if solution._shunt_elem._component_type == "L":
                    if solution._series_elem._component_type == "C":
                        Z2 = 1/(2*PI*freq*solution._series_elem._component_value.real) 
                        
        plt.plot(freq, Z2)
        
    def __repr__(self):
        rv  = f"From {self._Z1} Ω to {self._Z2} Ω\n\n"
        rv += f"normalized starting impedance = {self._Z1}Ω/{self._Z2}Ω = {self._normalized_impedance:.5g}\n\n"
        if len(self._solutions) > 0:
            rv += f"#solutions: {len(self._solutions)}\n\n"
            for solution in self._solutions:
                rv += f"{solution}"
        return rv



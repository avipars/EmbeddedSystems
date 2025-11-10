import numpy as np

class R2RNetwork:
    def __init__(self, r_value=10000):
        """
        Initialize R2R ladder network
        
        Args:
            r_value: Base resistance value in ohms (default 10kΩ)
        """
        self.R = r_value  # Base resistance
        self.num_bits = 3  # Three voltage sources (v1, v2, v3)
        self.speaker_load = 16  # 16 ohm speaker
        
    def calculate_thevenin_equivalent(self, v1, v2, v3):
        """
        Calculate Thevenin equivalent voltage and resistance for 3-bit R2R network
        
        Args:
            v1, v2, v3: Input voltages (LSB to MSB or vice versa)
        
        Returns:
            v_th: Thevenin equivalent voltage
            r_th: Thevenin equivalent resistance
        """
        # For a 3-bit R2R ladder, each bit contributes with binary weighting
        # Assuming v1 is MSB, v2 is middle bit, v3 is LSB
        # Contribution factors: 1/2, 1/4, 1/8
        
        v_th = (v1 / 2) + (v2 / 4) + (v3 / 8)
        
        # Thevenin resistance looking into the R2R network is R
        r_th = self.R
        
        return v_th, r_th
    
    def calculate_output_voltage(self, v1, v2, v3):
        """
        Calculate output voltage across the speaker
        
        Args:
            v1, v2, v3: Input voltages
        
        Returns:
            v_out: Output voltage across the speaker
            current: Current through the speaker
            power: Power dissipated in the speaker
        """
        # Get Thevenin equivalent
        v_th, r_th = self.calculate_thevenin_equivalent(v1, v2, v3)
        
        # Voltage divider with speaker load
        v_out = v_th * (self.speaker_load / (r_th + self.speaker_load))
        
        # Current through speaker
        current = v_out / self.speaker_load
        
        # Power dissipated in speaker
        power = v_out * current
        
        return v_out, current, power
    
    def display_results(self, v1, v2, v3):
        """Display detailed analysis results"""
        print("=" * 60)
        print("R2R LADDER DAC ANALYSIS")
        print("=" * 60)
        print(f"\nConfiguration:")
        print(f"  Base Resistance (R): {self.R/1000:.1f} kΩ")
        print(f"  Speaker Load: {self.speaker_load} Ω")
        print(f"\nInput Voltages:")
        print(f"  V1 (MSB): {v1:.3f} V")
        print(f"  V2:       {v2:.3f} V")
        print(f"  V3 (LSB): {v3:.3f} V")
        
        # Calculate Thevenin equivalent
        v_th, r_th = self.calculate_thevenin_equivalent(v1, v2, v3)
        print(f"\nThevenin Equivalent:")
        print(f"  V_th: {v_th:.6f} V")
        print(f"  R_th: {r_th/1000:.1f} kΩ")
        
        # Calculate output
        v_out, current, power = self.calculate_output_voltage(v1, v2, v3)
        print(f"\nOutput (across speaker):")
        print(f"  Voltage: {v_out:.6f} V")
        print(f"  Current: {current*1000:.6f} mA")
        print(f"  Power:   {power*1000:.6f} mW")
        print("=" * 60)
        
        return v_out


# Example usage
if __name__ == "__main__":
    # Create R2R network with 10kΩ resistors
    r2r = R2RNetwork(r_value=2000)
    
    # Example 1: All inputs at 5V (digital HIGH)
    print("\nExample 1: All bits HIGH (5V)")
    v_out1 = r2r.display_results(v1=5.0, v2=5.0, v3=5.0)
    
    # Example 2: Binary 101 pattern
    print("\n\nExample 2: Binary pattern 101")
    v_out2 = r2r.display_results(v1=5.0, v2=0.0, v3=5.0)
    
    # Example 3: Custom voltages
    print("\n\nExample 3: Custom voltages")
    v_out3 = r2r.display_results(v1=3.3, v2=1.5, v3=2.0)
    
    # Example 4: Generate truth table for 3-bit DAC with 5V logic
    print("\n\n" + "=" * 60)
    print("TRUTH TABLE (5V logic levels)")
    print("=" * 60)
    print(f"{'V1':>6} {'V2':>6} {'V3':>6} | {'V_out (V)':>12} | {'Binary':>6}")
    print("-" * 60)
    
    for i in range(8):
        v1 = 5.0 if (i & 0b100) else 0.0
        v2 = 5.0 if (i & 0b010) else 0.0
        v3 = 5.0 if (i & 0b001) else 0.0
        v_out, _, _ = r2r.calculate_output_voltage(v1, v2, v3)
        binary = f"{i:03b}"
        print(f"{v1:6.1f} {v2:6.1f} {v3:6.1f} | {v_out:12.6f} | {binary:>6}")
    
    print("=" * 60)
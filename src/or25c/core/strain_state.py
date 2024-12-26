# src/or25c/core/strain_state.py
from dataclasses import dataclass

@dataclass
class StrainState:
    """Principal strains and angle"""
    e1: float  # Principal tensile strain
    e2: float  # Principal compressive strain
    theta: float  # Angle of principal tensile strain from x-axis
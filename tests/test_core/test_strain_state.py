from or25c.core.strain_state import StrainState

def test_strain_state_creation():
    strain = StrainState(e1=0.001, e2=-0.002, theta=45.0)
    assert strain.e1 == 0.001
    assert strain.e2 == -0.002
    assert strain.theta == 45.0
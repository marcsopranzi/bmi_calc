
from bmi_calc import bmi_calculation
import pytest
import pandas as pd
from pandas.testing import assert_frame_equal

def test_bmi_calculation():
    # Arrange
    input = pd.DataFrame({'Gender':['Male', 'Male', 'Male', 'Female', 'Female', 'Female'], 
                        'HeightCm':[171, 161, 180, 166, 150, 167,], 
                        'WeightKg':[96, 85, 77, 62, 70, 82]
                       })
    expected = pd.DataFrame({'Gender':['Male', 'Male', 'Male', 'Female', 'Female', 'Female'], 
                            'HeightCm':[171, 161, 180, 166, 150, 167,], 
                            'WeightKg':[96, 85, 77, 62, 70, 82],
                            'BMI_index':[ 32.830615, 32.791945, 23.765432, 22.499637, 31.111111, 29.402273]
                            })
    # Act
    actual = bmi_calculation(input)
    # Assert
    assert_frame_equal(expected, actual)


import pandas as pd
from datetime import datetime

def initialize_fleet_data():
    data = [
        {
            "Reg": "TC-ABC",
            "MSN": 12345,
            "AC Type": "B737-800",
            "DOM": datetime(2012, 5, 15),
            "DOI": datetime(2013, 1, 1),
            "DOE": pd.NaT,
            "Lease Type": "OWN",
            "Lease End": pd.NaT
        },
        {
            "Reg": "TC-DEF",
            "MSN": 23456,
            "AC Type": "B737-8",
            "DOM": datetime(2019, 3, 20),
            "DOI": datetime(2019, 5, 1),
            "DOE": pd.NaT,
            "Lease Type": "OPS",
            "Lease End": datetime(2027, 5, 1)
        }
    ]
    return pd.DataFrame(data)

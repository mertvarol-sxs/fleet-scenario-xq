
import pandas as pd

def initialize_fleet_data():
    data = [
        {'Reg': f'TC-A{i:02d}', 'MSN': 10000 + i,
         'AC Type': ac_type,
         'DOM': pd.Timestamp(f'{2010+i%10}-0{(i%5)+1}-10'),
         'DOI': pd.Timestamp(f'{2011+i%10}-0{(i%5)+2}-20'),
         'DOE': pd.NaT,
         'Lease Type': lease_type,
         'Lease End': pd.Timestamp(f'{2028+i%5}-01-01') if lease_type == 'OPS' else pd.NaT}
        for i, (ac_type, lease_type) in enumerate(zip(
            ['B737-800', 'B737-8', 'B737-10', 'A320neo', 'A321neo']*4,
            ['OPS', 'FIN', 'OWN', 'OPS', 'FIN']*4
        ), 1)
    ]
    return pd.DataFrame(data)

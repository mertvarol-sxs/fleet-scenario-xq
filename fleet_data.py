
import pandas as pd

def initialize_fleet_data():
    data = [
        {'Reg': 'TC-A01', 'MSN': 10001, 'AC Type': 'B737-8', 'DOM': pd.Timestamp('2011-02-10'), 'DOI': pd.Timestamp('2012-02-20'), 'DOE': pd.NaT, 'Lease Type': 'OPS', 'Lease End': pd.Timestamp('2029-01-01')},
        {'Reg': 'TC-A02', 'MSN': 10002, 'AC Type': 'B737-10', 'DOM': pd.Timestamp('2012-03-10'), 'DOI': pd.Timestamp('2013-03-20'), 'DOE': pd.NaT, 'Lease Type': 'FIN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A03', 'MSN': 10003, 'AC Type': 'A320neo', 'DOM': pd.Timestamp('2013-04-10'), 'DOI': pd.Timestamp('2014-04-20'), 'DOE': pd.NaT, 'Lease Type': 'OWN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A04', 'MSN': 10004, 'AC Type': 'A321neo', 'DOM': pd.Timestamp('2014-05-10'), 'DOI': pd.Timestamp('2015-05-20'), 'DOE': pd.NaT, 'Lease Type': 'OPS', 'Lease End': pd.Timestamp('2032-01-01')},
        {'Reg': 'TC-A05', 'MSN': 10005, 'AC Type': 'B737-800', 'DOM': pd.Timestamp('2015-06-10'), 'DOI': pd.Timestamp('2016-06-20'), 'DOE': pd.NaT, 'Lease Type': 'FIN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A06', 'MSN': 10006, 'AC Type': 'B737-8', 'DOM': pd.Timestamp('2016-07-10'), 'DOI': pd.Timestamp('2017-07-20'), 'DOE': pd.NaT, 'Lease Type': 'OWN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A07', 'MSN': 10007, 'AC Type': 'B737-10', 'DOM': pd.Timestamp('2017-08-10'), 'DOI': pd.Timestamp('2018-08-20'), 'DOE': pd.NaT, 'Lease Type': 'OPS', 'Lease End': pd.Timestamp('2030-01-01')},
        {'Reg': 'TC-A08', 'MSN': 10008, 'AC Type': 'A320neo', 'DOM': pd.Timestamp('2018-09-10'), 'DOI': pd.Timestamp('2019-09-20'), 'DOE': pd.NaT, 'Lease Type': 'FIN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A09', 'MSN': 10009, 'AC Type': 'A321neo', 'DOM': pd.Timestamp('2019-10-10'), 'DOI': pd.Timestamp('2020-10-20'), 'DOE': pd.NaT, 'Lease Type': 'OWN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A10', 'MSN': 10010, 'AC Type': 'B737-800', 'DOM': pd.Timestamp('2010-11-10'), 'DOI': pd.Timestamp('2011-11-20'), 'DOE': pd.NaT, 'Lease Type': 'OPS', 'Lease End': pd.Timestamp('2028-01-01')},
        {'Reg': 'TC-A11', 'MSN': 10011, 'AC Type': 'B737-8', 'DOM': pd.Timestamp('2011-01-10'), 'DOI': pd.Timestamp('2012-01-20'), 'DOE': pd.NaT, 'Lease Type': 'FIN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A12', 'MSN': 10012, 'AC Type': 'B737-10', 'DOM': pd.Timestamp('2012-02-10'), 'DOI': pd.Timestamp('2013-02-20'), 'DOE': pd.NaT, 'Lease Type': 'OWN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A13', 'MSN': 10013, 'AC Type': 'A320neo', 'DOM': pd.Timestamp('2013-03-10'), 'DOI': pd.Timestamp('2014-03-20'), 'DOE': pd.NaT, 'Lease Type': 'OPS', 'Lease End': pd.Timestamp('2031-01-01')},
        {'Reg': 'TC-A14', 'MSN': 10014, 'AC Type': 'A321neo', 'DOM': pd.Timestamp('2014-04-10'), 'DOI': pd.Timestamp('2015-04-20'), 'DOE': pd.NaT, 'Lease Type': 'FIN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A15', 'MSN': 10015, 'AC Type': 'B737-800', 'DOM': pd.Timestamp('2015-05-10'), 'DOI': pd.Timestamp('2016-05-20'), 'DOE': pd.NaT, 'Lease Type': 'OWN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A16', 'MSN': 10016, 'AC Type': 'B737-8', 'DOM': pd.Timestamp('2016-06-10'), 'DOI': pd.Timestamp('2017-06-20'), 'DOE': pd.NaT, 'Lease Type': 'OPS', 'Lease End': pd.Timestamp('2029-01-01')},
        {'Reg': 'TC-A17', 'MSN': 10017, 'AC Type': 'B737-10', 'DOM': pd.Timestamp('2017-07-10'), 'DOI': pd.Timestamp('2018-07-20'), 'DOE': pd.NaT, 'Lease Type': 'FIN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A18', 'MSN': 10018, 'AC Type': 'A320neo', 'DOM': pd.Timestamp('2018-08-10'), 'DOI': pd.Timestamp('2019-08-20'), 'DOE': pd.NaT, 'Lease Type': 'OWN', 'Lease End': pd.NaT},
        {'Reg': 'TC-A19', 'MSN': 10019, 'AC Type': 'A321neo', 'DOM': pd.Timestamp('2019-09-10'), 'DOI': pd.Timestamp('2020-09-20'), 'DOE': pd.NaT, 'Lease Type': 'OPS', 'Lease End': pd.Timestamp('2032-01-01')},
        {'Reg': 'TC-A20', 'MSN': 10020, 'AC Type': 'B737-800', 'DOM': pd.Timestamp('2010-10-10'), 'DOI': pd.Timestamp('2011-10-20'), 'DOE': pd.NaT, 'Lease Type': 'FIN', 'Lease End': pd.NaT}
    ]
    return pd.DataFrame(data)

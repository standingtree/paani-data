import pandas as pd
# ------------------------------------------------------------------------------------------------------------ #
# RAW DATA --------------------------------------------------------------------------------------------------- #
# ------------------------------------------------------------------------------------------------------------ #

# load long-form dataframe
dataFilepath = 'C:/Users/viren/Documents/_MSFM/water index'

# rainfall data
rf_data = pd.read_excel(dataFilepath + r'/_consolidated data/actual_rf_all_states.xlsx', index_col=0)

# groundwater data
gw_data = pd.read_excel(dataFilepath + r'/_consolidated data/groundwater_levels_all_states.xlsx', index_col=0)

# reservoir storage data
res_data = pd.read_excel(dataFilepath + r'/_consolidated data/reservoir_storage_all_states.xlsx', index_col=0)

# pricing data
price_data = pd.read_excel(dataFilepath + r'/_consolidated data/consolidated_prices.xlsx')

# codes
state_codes = pd.read_excel(dataFilepath + r'/State-Basin-Codes.xlsx', sheet_name='States',index_col=3)
code_for_state = dict(zip(state_codes['State'], state_codes.index))
basin_codes = pd.read_excel(dataFilepath + r'/State-Basin-Codes.xlsx', sheet_name='RiverBasins',index_col=3)
city_state = dict(pd.read_excel(dataFilepath + r'/State-Basin-Codes.xlsx', sheet_name='CityState',index_col=0))
print("Loading data...\n",state_codes.head(), basin_codes.head(), city_state)
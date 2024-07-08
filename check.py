import pandas as pd

# pandas.read_excel('excel's name + .xlsx', sheet_name = 'sheet's name')
control = pd.read_excel('simple_data.xlsx', sheet_name = 'control')
info = pd.read_excel('simple_data.xlsx', sheet_name = 'info')
rfi = pd.read_excel('simple_data.xlsx', sheet_name = 'rfi')

# pandas.Series.str.split('get rid and split')
info['info_mapping'] = info['info_mapping'].str.split(';')
# pandas.DataFrame.explode('') -> index: 00112233
info_exploded = info.explode('info_mapping')
# isin -> new Boolean Series
# df[~df['name'].isin(2df['2name'])] generate Series that only not in 2df2name value row
info_unmatched = info_exploded[~info_exploded['info_mapping'].isin(control['ref_id'])]

# same rfi
rfi['rfi_mapping'] = rfi['rfi_mapping'].str.split(';')
rfi_exploded = rfi.explode('rfi_mapping')
rfi_unmatched = rfi_exploded[~rfi_exploded['rfi_mapping'].isin(control['ref_id'])]

# 2 Series ok last one
# combine info & rfi prepare for control
combined_mappings = pd.concat([info_exploded['info_mapping'], rfi_exploded['rfi_mapping']]).unique()

# similar to up
control_unmatched = control[~control['ref_id'].isin(combined_mappings)]

# concat again to result
result = pd.concat([control_unmatched, rfi_unmatched, control_unmatched])

print(result)
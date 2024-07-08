import pandas as pd

# 讀取Excel文件中的各個sheet
control = pd.read_excel('SWIFT_Framework.xlsx', sheet_name='control')
info = pd.read_excel('SWIFT_Framework.xlsx', sheet_name='info')
rfi = pd.read_excel('SWIFT_Framework.xlsx', sheet_name='rfi')

# 將info_mapping和rfi_mapping展開為單獨的值
info['info_mapping'] = info['info_mapping'].str.split(';')
rfi['rfi_mapping'] = rfi['rfi_mapping'].str.split(';')

# 將info和rfi的展開的值與control的ref_id進行比對
info_matches = info.explode('info_mapping')
info_matches = info_matches[~info_matches['info_mapping'].isin(control['ref_id'])]

rfi_matches = rfi.explode('rfi_mapping')
rfi_matches = rfi_matches[~rfi_matches['rfi_mapping'].isin(control['ref_id'])]

# 找出control中沒有匹配到info或rfi的行
control_matches = control[~control['ref_id'].isin(info_matches['info_mapping']) & ~control['ref_id'].isin(rfi_matches['rfi_mapping'])]

# 按照control, info, rfi的順序輸出結果
result = pd.concat([control_matches, info_matches, rfi_matches])

# 輸出結果
print(result)
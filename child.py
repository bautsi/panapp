import pandas as pd

# 讀取Excel文件中的control工作表
control = pd.read_excel('SWIFT_Framework.xlsx', sheet_name='control')

# 確保 depth 欄位是數字類型
control['depth'] = control['depth'].astype(int)

# 計算每個ref_id的子層級數量
def calculate_children(control):
    result = {row['ref_id']: 0 for _, row in control.iterrows()}

    for i, row in control.iterrows():
        current_ref_id = row['ref_id']
        current_depth = row['depth']
        
        for j in range(i + 1, len(control)):
            next_ref_id = control.loc[j, 'ref_id']
            next_depth = control.loc[j, 'depth']
            
            if next_depth > current_depth:
                result[current_ref_id] += 1
            else:
                break

    return result

result = calculate_children(control)

# 將結果轉換為DataFrame並輸出
result_control = pd.DataFrame(list(result.items()), columns=['ref_id', 'child_count'])
print(result_control)

# 如果需要將結果保存到Excel文件
result_control.to_excel('result_control.xlsx', index=False)
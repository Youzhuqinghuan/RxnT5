import pandas as pd
from rdkit import Chem

def is_valid_smiles(smiles):
    """
    检查给定的 SMILES 是否有效。
    返回 True 表示合法，False 表示非法。
    """
    try:
        if pd.isna(smiles) or smiles.strip() == '':
            return False
        mol = Chem.MolFromSmiles(smiles)
        return mol is not None
    except Exception:
        return False

def check_dataset(file_path):
    """
    检查数据集中 'Biaryl', 'Olefin', 'Solvent', 'Product' 列的有效性。
    - 'Olefin' 列允许为空；
    - 其他列不允许为空，且必须为合法 SMILES。
    """
    # 读取数据
    df = pd.read_csv(file_path)
    
    # 初始化记录非法行的 DataFrame
    invalid_rows = pd.DataFrame()

    # 检查 'Biaryl', 'Solvent', 'Product' 是否为合法 SMILES 且不能为空
    for col in ['Biaryl', 'Solvent', 'Product']:
        invalid = df[~df[col].apply(is_valid_smiles)]
        if not invalid.empty:
            invalid_rows = pd.concat([invalid_rows, invalid], axis=0)
            print(f"列 '{col}' 存在非法值：")
            print(invalid[['Biaryl', 'Olefin', 'Solvent', 'Product']])

    # 检查 'Olefin' 是否为合法 SMILES（允许为空）
    invalid_olefin = df[~df['Olefin'].isna() & ~df['Olefin'].apply(is_valid_smiles)]
    if not invalid_olefin.empty:
        invalid_rows = pd.concat([invalid_rows, invalid_olefin], axis=0)
        print("列 'Olefin' 存在非法值：")
        print(invalid_olefin[['Biaryl', 'Olefin', 'Solvent', 'Product']])

    # 输出最终不符合要求的行
    if not invalid_rows.empty:
        invalid_rows = invalid_rows.drop_duplicates()
        print("\n最终不符合要求的行：")
        print(invalid_rows[['Biaryl', 'Olefin', 'Solvent', 'Product']])
        return invalid_rows
    else:
        print("所有数据均合法！")
        return None

# 指定文件路径
file_path = '/home/hcp/Chem/Dataset/datav2.csv'
invalid_data = check_dataset(file_path)

# 如果需要保存非法行信息
if invalid_data is not None:
    invalid_data.to_csv('./data/invalid_rows.csv', index=False)

import csv
import random

# 读取原始CSV文件
input_file = './data/datav2.csv'
output_file = './data/data.csv'

# 定义划分比例
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# 读取原始CSV文件
with open(input_file, mode='r') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

# 打乱数据顺序
random.shuffle(rows)

# 计算划分点
total_rows = len(rows)
train_end = int(total_rows * train_ratio)
val_end = train_end + int(total_rows * val_ratio)

# 划分数据集
train_set = rows[:train_end]
val_set = rows[train_end:val_end]
test_set = rows[val_end:]

# 写入训练集
with open(output_file.replace('.csv', '_train.csv'), mode='w', newline='') as trainfile:
    writer = csv.writer(trainfile)
    writer.writerow(['REACTANT', 'REAGENT', 'PRODUCT', 'YIELD'])  # 写入表头
    for row in train_set:
        reactant = row['Biaryl']
        if row['Olefin']:
            reactant += f".{row['Olefin']}"
        reagent = row['Solvent'] if row['Solvent'] else " "
        product = row['Product']
        yield_value = row['Yeild']
        writer.writerow([reactant, reagent, product, yield_value])

# 写入验证集
with open(output_file.replace('.csv', '_val.csv'), mode='w', newline='') as valfile:
    writer = csv.writer(valfile)
    writer.writerow(['REACTANT', 'REAGENT', 'PRODUCT', 'YIELD'])  # 写入表头
    for row in val_set:
        reactant = row['Biaryl']
        if row['Olefin']:
            reactant += f".{row['Olefin']}"
        reagent = row['Solvent'] if row['Solvent'] else " "
        product = row['Product']
        yield_value = row['Yeild']
        writer.writerow([reactant, reagent, product, yield_value])

# 写入测试集
with open(output_file.replace('.csv', '_test.csv'), mode='w', newline='') as testfile:
    writer = csv.writer(testfile)
    writer.writerow(['REACTANT', 'REAGENT', 'PRODUCT', 'YIELD'])  # 写入表头
    for row in test_set:
        reactant = row['Biaryl']
        if row['Olefin']:
            reactant += f".{row['Olefin']}"
        reagent = row['Solvent'] if row['Solvent'] else " "
        product = row['Product']
        yield_value = row['Yeild']
        writer.writerow([reactant, reagent, product, yield_value])

print(f"转换完成，结果已保存到 {output_file.replace('.csv', '_train.csv')}, {output_file.replace('.csv', '_val.csv')}, {output_file.replace('.csv', '_test.csv')}")
# ライブラリをインポートする
import openpyxl

# 新規にワークブックを作成する
wb = openpyxl.Workbook()

# 新規にワークシートを作成する
ws = wb.create_sheet(title='sales')

# 既存のシートを削除
wb.remove(wb['Sheet'])

# 保存する
wb.save('sales.xlsx')

# 閉じる
wb.close()
# 入力を得てインチをセンチメートルに変換（未完成）
# 変換の元になる値
per_inch = 2.54

# ユーザから入力を得る
user = input("inch? ")

# 浮動小数点型に玄関
inch = float(user)

# 結果を表示
cm = inch * per_inch
print(cm)

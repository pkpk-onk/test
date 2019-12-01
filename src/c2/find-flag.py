# for幸便をフラグで分岐する場合
# お弁当の食材データからリストを作成
foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

# マンゴーがないか確認する
flag_found = False #マンゴーがいないかを確認する変数。初期値False
for food in foodstuff :
    if food == "Mango" :
        flag_found = True
        break

if flag_found :
    print("マンゴーが入ってます")
else :
    print("ありません")

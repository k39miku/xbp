 name="aaa"
waist=84
age=44

print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")

if waist>=85:
    print(name,"さん、内臓脂肪蓄積注意です")
else:
    print(name,"さん、腹囲は問題ありません")
for i in range(3): #コロンが入っていることに注意
     print(i,"人目") #タブでずらしていることに注意！

    # 出力結果
    # 0 人目
    # 1 人目
    # 2 人目

    #文字だからダブルクォーテーション

    name=input("名前を教えて下さい")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))


    #ここから先はプリント
    print(name,"三は腹囲",waist,"cmで年齢は",age,"才ですね")


    #ここから先は条件分岐
    if waist>=85 and age>=40:
    print (name, "さん、内臓脂肪蓄積注意です")
    else:
    print (name, "さんは内臓脂肪は問題ありません。")


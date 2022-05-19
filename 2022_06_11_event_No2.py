def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):
    chk=0
    #pl:left index pr:right index
    pl=0
    pr=len(sorted_array)-1

    # plとprの差が1になるまで二部探索
    while pl+1 < pr:
        pc=(pl+pr)//2  #pc:center index
        # 配列のpc要素より、target_numberが大きい場合はplをpcに更新する
        if sorted_array[pc] < target_number:
            pl=pc
        # 配列のpc要素より、target_numberが小さい場合はprをpcに更新する
        elif sorted_array[pc] > target_number:
            pr=pc
        # 配列のpc要素がtarget_numberの場合はplをpcを出力
        else:
            chk=1
            return pc
            break
    # 二部探索中にpc要素がtarget_numberにならなかった場合、pl要素かpr要素がtarget_numberであるか判定し、一致したら出力
    if chk==0:
        if sorted_array[pl]==target_number:
            return pl
        elif sorted_array[pr]==target_number:
            return pr
    
    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
def main():
    #ランダムに並べられた重複のない整数の配列
    array = [11, 5, 4, 6, 2, 1, 9, 8, 3, 7, 10]
    # ソート実行
    sortedArray = sort(array)
    # 結果出力
    [print(i) for i in sortedArray]

def sort(array):
    # 要素が一つの場合はソートの必要がないので、そのまま返却
    if len(array) == 1:
        return array

    # 配列の先頭を基準値とする
    #if len(array) ==2:
    #    if array[0] > array[1]:
    #        array[0],array[1] = array[1],array[0]
    #
    #    return array

    pivot = array[0]
    p_front=0
    p_back=len(array)-1
    while p_front < p_back:
        if array[p_front] >= pivot and array[p_back] < pivot:
            array[p_front],array[p_back] = array[p_back],array[p_front]
        elif array[p_front] >= pivot:
            p_back-=1
        elif array[p_back] < pivot:
            p_front+=1
        else:
            p_front+=1
            p_back-=1

    back_start=0

    if p_front==p_back and p_front==0:
        back_start=1
    elif p_front==p_back:
        if array[p_front] >= pivot:
            back_start = p_front
        else:
            back_start = p_front+1
    else:
        back_start = p_front

    array_front = array[0:back_start]
    array_back = array[back_start:len(array)]
    #print(array_front,array_back)
    if len(array_front) >=1:
        sorted_array_front = sort(array_front)
    if len(array_back) >=1:    
        sorted_array_back = sort(array_back)
    
    new_array = sorted_array_front
    new_array.extend(sorted_array_back)
    
    return new_array

if __name__ == '__main__':
    main()
import csv

def inventory_lst():
    with open('C:\Codyssey\project4-2\Mars_Base_Inventory_List.csv', 'r', encoding='utf-8') as f :
        inven_lst = f.readlines()
        inven_csv = "".join(inven_lst)

        inven_parsing_lst = []
        for oneline in inven_lst:
            oneline = oneline.strip('\n').split(',')
            inven_parsing_lst.append(oneline)

        sorted_lst = sorted(inven_parsing_lst, key=lambda x: x[4], reverse=True)

    return inven_csv, inven_parsing_lst, sorted_lst

def danger_filtered(lst):
    del lst[0]
    danger_lst = []
    for oneline in lst:
        if float(oneline[4]) >= 0.7:
            danger_lst.append(oneline)
    

    with open('C:\Codyssey\project4-2\Mars_Base_Inventory_danger.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(danger_lst)

    return danger_lst

def two_dimension_lst(lst):
    for i in lst:
        for j in i:
            print(str(j), end=' ')
        print()

def main():
    inven_csv, inven_parsing_lst, sorted_lst = inventory_lst()
    print(f'csv 전체 내용 출력\n{inven_csv}')
    print(f'\ncsv -> list 객체 변환 후 출력\n{inven_parsing_lst}')
    print('\nlist를 flammability index 기준 내림차순 정렬 후 출력')
    two_dimension_lst(sorted_lst)

    danger_lst = danger_filtered(sorted_lst)
    print('\n인화성 지수 0.7 이상인 항목 출력 후 csv파일로 저장')
    two_dimension_lst(danger_lst)


if __name__ == '__main__':
    main()
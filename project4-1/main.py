import json

def log_read():
    try:
        LogFile = open('C:\Codyssey\project4-1\mission_computer_main.log', 'r') #문자열로 저장됨
        LogFile = LogFile.read()
        print(LogFile)

    except FileNotFoundError:
        print('파일을 찾을 수 없습니다.')
        return
    except Exception as e:
        print('파일 읽는 중 오류 발생 : ', str(e))
        return
    
    return LogFile

def log_split():
    LogFile = open('C:\Codyssey\project4-1\mission_computer_main.log', 'r')
    lines = LogFile.readlines()
    del lines[0]

    newlines = []
    for oneline in lines:
        oneline = oneline.strip('\n').split(',')
        del oneline[1]
        newlines.append(oneline)

    return newlines

def log_sort(logfile):
    sortedlog = sorted(logfile, key=lambda x: x[0], reverse=True)
    return sortedlog

def lst_to_dict(lst):
    LogDict = dict(lst)
    return LogDict

def dict_to_json(dict):
    f = open('C:\Codyssey\project4-1\mission_computer_main.json', 'w', encoding='utf-8')
    json.dump(dict, f, indent=4)

def bonus(dict):
    try:
        with open('C:\Codyssey\project4-1\mission_computer_main.log', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        sorted_log = sorted(lines, key=lambda line: line[1:20], reverse=True)
        print('로그 파일 역순 정렬 출력')
        for line in sorted_log:
            print(line.strip('\n'))
    except Exception as e:
        print('파일 읽는 중 오류 발생 : ', str(e))

    danger_dict = {}
    for key, value in dict.items():
        for dword in ['unstable', 'explosion', 'leak', 'overheating']:
            if dword in value:
                danger_dict[key] = value
                break
    f = open('C:\Codyssey\project4-1\\filtered_mission_computer_main.json', 'w', encoding='utf-8')
    json.dump(danger_dict, f, indent=4)

    message = input("mission_computer_main파일에서 검색하고 싶은 문자열을 입력하세요. : ")
    message = message.lower()
    for key, value in dict.items():
        str_value = str(value).lower()
        if message in str_value:
            print(f'\n{key} : {value}')

def main():
    print('\nlog파일 읽기\n')
    LogFile = log_read()

    print('\nlog파일 리스트로 만들기\n')
    lines = log_split()
    print(lines)

    print('\nlog파일 내림차순 정렬\n')
    sortedlog = log_sort(lines)
    for i in sortedlog:
        for j in i:
            print(str(j), end=' ')
        print()

    print('\n리스트-딕셔너리 변환\n')
    LogDict = lst_to_dict(lines)
    for key, value in LogDict.items():
        print(f'{key} : {value}')

    print('\njson파일 생성\n')
    dict_to_json(LogDict)

    print('-------------- 보너스 과제 ----------------')
    bonus(LogDict)

if __name__ == '__main__':
    main()
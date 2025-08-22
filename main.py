def log_read():
    try:
        LogFile = open("C:\Codyssey\mission_computer_main.log", 'r') #문자열로 저장됨
        LogFile = LogFile.read()
        print(LogFile)

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return
    except Exception as e:
        print("파일 읽는 중 오류 발생 : ", str(e))
        return
    
    LogFile.close()
    return LogFile

def log_to_list(logfile):
    LogList = []
    LogList = logfile.split(",")

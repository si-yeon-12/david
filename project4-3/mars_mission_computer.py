import random
import json
import time
import platform
import os
import psutil
import threading
import multiprocessing

class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,    # 내부 온도 (도)
            'mars_base_external_temperature': None,    # 외부 온도 (도)
            'mars_base_internal_humidity': None,       # 내부 습도 (%)
            'mars_base_external_illuminance': None,    # 외부 광량 (W/m2)
            'mars_base_internal_co2': None,            # 내부 CO2 농도 (%)
            'mars_base_internal_oxygen': None          # 내부 산소 농도 (%)
        }

    def set_env(self):
        try:
            self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
            self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
            self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
            self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
            self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 3)
            self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)
        except Exception as e:
            print(f'환경 데이터 설정 중 오류 발생: {e}')

    def get_env(self):
        return self.env_values
    
class MissionComputer:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': None,
            'mars_base_external_temperature': None,
            'mars_base_internal_humidity': None,
            'mars_base_external_illuminance': None,
            'mars_base_internal_co2': None,
            'mars_base_internal_oxygen': None
        }
        self.ds = DummySensor()

    def get_sensor_data(self):
        try:
            while True:
                self.ds.set_env()
                self.env_values = self.ds.get_env()
                json_data = json.dumps(self.env_values, indent=4, ensure_ascii=False)
                print(f'\n화성 기지 환경 데이터 (JSON 형식):\n{json_data}')
                time.sleep(5) # 5초 대기
        except KeyboardInterrupt:
            print('센서 데이터 수집 중단됨.')  
        except Exception as e:
            print(f'센서 데이터 수집 중 오류 발생: {e}')

    def get_mission_computer_info(self):
        try:
            info = {
                '운영체제' : platform.system(),
                '운영체제 버전' : platform.version(),
                'cpu_타입' : platform.processor(),
                'cpu_코어_수' : os.cpu_count(),
                '메모리_총_크기(GB)' : round(psutil.virtual_memory().total / (1024 ** 3), 2),
            }
            json_info = json.dumps(info, indent=4, ensure_ascii=False)
            print('\n화성 미션 컴퓨터 정보 (JSON 형식):')
            print(json_info)
            return info

        except Exception as e:
            print(f'컴퓨터 정보 수집 중 오류 발생: {e}')

    def get_mission_computer_load(self):
        try:
            load = {
                'cpu_사용률(%)' : psutil.cpu_percent(interval=1),
                '메모리_사용률(%)' : psutil.virtual_memory().percent,
            }
            json_load = json.dumps(load, indent=4, ensure_ascii=False)
            print('\n화성 미션 컴퓨터 부하 정보 (JSON 형식):')
            print(json_load)
            return load
        except Exception as e:
            print(f'컴퓨터 부하 수집 중 오류 발생: {e}')
            
def run_threads():
    print("멀티 스레드 실행 시작")
    RunComputer = MissionComputer(name='Threaded_MissionComputer')

    t1 = threading.Thread(target=RunComputer.get_sensor_data)
    t2 = threading.Thread(target=RunComputer.get_mission_computer_info)
    t3 = threading.Thread(target=RunComputer.get_mission_computer_load)

    t1.start()
    t2.start()
    t3.start()

def run_processes():
    print("멀티 프로세스 실행 시작")

    runComputer1 = MissionComputer(name='Process_MissionComputer_1')
    runComputer2 = MissionComputer(name='Process_MissionComputer_2')
    runComputer3 = MissionComputer(name='Process_MissionComputer_3')

    p1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info)
    p2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load)
    p3 = multiprocessing.Process(target=runComputer3.get_sensor_data)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()


if __name__ == '__main__':
    # RunComputer = MissionComputer()
    # RunComputer.get_sensor_data()
    # RunComputer.get_mission_computer_info()
    # RunComputer.get_mission_computer_load()
    run_threads()
    # run_processes()
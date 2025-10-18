import random

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

if __name__ == '__main__':
    ds = DummySensor()
    ds.set_env()
    env_data = ds.get_env()

    print('현재 화성 기지 환경 데이터:')
    for key, value in env_data.items():
        print(f'{key}: {value}')

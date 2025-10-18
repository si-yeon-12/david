# 문제 2. 미션 컴퓨터 제작
수행 과제
미션 컴퓨터에 해당하는 클래스를 생성한다. 클래스의 이름은 MissionComputer로 정의한다.
미션 컴퓨터에는 화성 기지의 환경에 대한 값을 저장할 수 있는 딕서너리 객체가 env_values라는 속성으로 포함되어야 한다.
env_values라는 속성 안에는 다음과 같은 내용들이 구현 되어야 한다.
화성 기지 내부 온도 (mars_base_internal_temperature)
화성 기지 외부 온도 (mars_base_external_temperature)
화성 기지 내부 습도 (mars_base_internal_humidity)
회성 기지 외부 광량 (mars_base_external_illuminance)
화성 기지 내부 이산화탄소 농도 (mars_base_internal_co2)
화성 기지 내부 산소 농도 (mars_base_internal_oxygen)
문제 3에서 제작한 DummySensor 클래스를 ds라는 이름으로 인스턴스화 시킨다.
MissionComputer에 get_sensor_data() 메소드를 추가한다.
get_sensor_data() 메소드에 다음과 같은 세 가지 기능을 추가한다.
센서의 값을 가져와서 env_values에 담는다.
env_values의 값을 출력한다. 이때 환경 정보의 값은 json 형태로 화면에 출력한다.
위의 두 가지 동작을 5초에 한번씩 반복한다.
MissionComputer 클래스를 RunComputer 라는 이름으로 인스턴스화 한다.
RunComputer 인스턴스의 get_sensor_data() 메소드를 호출해서 지속적으로 환경에 대한 값을 출력 할 수 있도록 한다.
전체 코드를 mars_mission_computer.py 파일로 저장한다.
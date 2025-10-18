# 문제 1. 더미 센서 제작
수행 과제
더미 센서에 해당하는 클래스를 생성한다. 클래스의 이름은 DummySensor로 정의한다.
DummySensor의 멤버로 env_values라는 딕서너리를 추가한다. 딕셔너리에는 다음과 같은 항목들이 추가 되어 있어야 한다.

화성 기지 내부 온도 (mars_base_internal_temperature)
화성 기지 외부 온도 (mars_base_external_temperature)
화성 기지 내부 습도 (mars_base_internal_humidity)
회성 기지 외부 광량 (mars_base_external_illuminance)
화성 기지 내부 이산화탄소 농도 (mars_base_internal_co2)
화성 기지 내부 산소 농도 (mars_base_internal_oxygen)

DummySensor는 테스트를 위한 객체이므로 데이터를 랜덤으로 생성한다.
DummySensor 클래스에 set_env() 메소드를 추가한다. set_env() 메소드는 random으로 주어진 범위 안의 값을 생성해서 env_values 항목에 채워주는 역할을 한다. 각 항목의 값의 범위는 다음과 같다.

화성 기지 내부 온도 (18~30도)
화성 기지 외부 온도 (0~21도)
화성 기지 내부 습도 (50~60%)
화성 기지 외부 광량 (500~715 W/m2)
화성 기지 내부 이산화탄소 농도 (0.02~0.1%)
화성 기지 내부 산소 농도 (4%~7%)

DummySensor 클래스는 get_env() 메소드를 추가하는데 get_env() 메소드는 env_values를 return 한다.
DummySensor 클래스를 ds라는 이름으로 인스턴스(Instance)로 만든다.
인스턴스화 한 DummySensor 클래스에서 set_env()와 get_env()를 차례로 호출해서 값을 확인한다.
전체 코드를 mars_mission_computer.py 파일로 저장한다.

	
# 제약사항
Python에서 기본 제공되는 명령어만 사용해야 하며 별도의 라이브러리나 패키지를 사용해서는 안된다.
random, 시간을 다루는 라이브러리 및 시스템 정보를 가져오는 라이브러리는 사용 가능하다.
쓰레드와 멀티 프로세스를 다루는 부분은 외부 라이브러리 사용 가능하다.
Python의 coding style guide를 확인하고 가이드를 준수해서 코딩한다.
경고 메시지 없이 모든 코드는 실행 되어야 한다.
시스템 정보를 가져오는 부분은 예외처리가 되어 있어야 한다.
모든 라이브러리는 안정된 마지막 버전을 사용해야 한다.

Python 버전은 3.x 버전으로 한다.
Python의 coding style guide를 확인하고 가이드를 준수해서 코딩한다. 
(PEP 8 – 파이썬 코드 스타일 가이드 | peps.python.org)
문자열을 표현 할 때에는 ‘ ’을 기본으로 사용한다. 다만 문자열 내에서 ‘을 사용할 경우와 같이 부득이한 경우에는 “ “를 사용한다.
foo = (0,) 와 같이 대입문의 = 앞 뒤로는 공백을 준다.
들여 쓰기는 공백을 기본으로 사용합니다.
# 문제 4. 미션 컴퓨터 개선
# 수행과제
# 값들을 연속적으로 출력하기 위해서 MissionComputer 클래스에 있는 get_mission_computer_info(), get_mission_computer_load() 두 개의 메소드를 time 라이브러리를 사용해서 각각 20초에 한번씩 결과를 출력 할 수 있게 수정한다.
# MissionComputer 클래스를 runComputer 라는 이름으로 인스턴스화 한다.
# runComputer 인스턴스의 get_mission_computer_info(), get_mission_computer_load(), get_sensor_data() 메소드를 각각 멀티 쓰레드로 실행 시킨다.
# 다시 코드를 수정해서 MissionComputer 클래스를 runComputer1, runComputer2, runComputer3 이렇게 3개의 인스턴스를 만든다.
# 3개의 인스턴스를 멀티 프로세스로 실행시켜서 각각 get_mission_computer_info(), get_mission_computer_load(), get_sensor_data()를 실행시키고 출력을 확인한다.
# 최종적으로 결과를 mars_mission_computer.py 에 저장한다.
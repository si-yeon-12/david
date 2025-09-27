import numpy as np

def read_csv_parts_and_strength(filename):
    try:
        # dtype='str'로 읽어서 2차원 배열로 반환
        data = np.genfromtxt(filename, delimiter=',', dtype='str', skip_header=1)
        parts = data[:, 0]
        strength = data[:, 1].astype(float)
        return parts, strength
    except FileNotFoundError:
        print(f"[파일 읽기 오류] 파일을 찾을 수 없습니다: {filename}")
        return None, None
    except Exception as e:
        print(f"[알 수 없는 오류] '{filename}' 처리 중 문제가 발생했습니다: {e}")
        return None, None

def analyze_and_filter_parts(filenames):
    parts_list = []
    strengths_list = []
    for fname in filenames:
        parts, strengths = read_csv_parts_and_strength(fname)
        if parts is None or strengths is None:
            return
        parts_list.append(parts)
        strengths_list.append(strengths)

    try:
        # 부품명은 첫 파일 기준(모두 동일하다고 가정)
        parts = parts_list[0]
        strengths = np.vstack(strengths_list)
        averages = np.mean(strengths, axis=0)
        print("항목별 평균값:", np.round(averages, 3))

        # 평균값 50 미만 항목 필터링
        filter_mask = averages < 50
        if not np.any(filter_mask):
            print("평균값이 50 미만인 항목이 없음")
            return

        filtered_parts = parts[filter_mask]
        filtered_averages = averages[filter_mask]

        # 저장
        output_filename = 'parts_to_work_on.csv'
        try:
            # 1열: 부품명, 2열: 평균값
            result = np.column_stack((filtered_parts, np.round(filtered_averages, 3)))
            np.savetxt(output_filename, result, delimiter=",", fmt='%s')
            print(f"성공: 필터링된 부품명과 평균값을 '{output_filename}' 파일로 저장했습니다.")
        except Exception as e:
            print(f"[파일 저장 오류] '{output_filename}' 저장 중 문제가 발생했습니다: {e}")

    except Exception as e:
        print(f"[알 수 없는 오류] 데이터 처리 중 문제가 발생했습니다: {e}")

def main():
    csv_files = [
        'mars_base_main_parts-001.csv',
        'mars_base_main_parts-002.csv',
        'mars_base_main_parts-003.csv'
    ]

    while True:
        analyze_and_filter_parts(csv_files)
        user_input = input("\n분석을 다시 실행하려면 Enter를, 종료하려면 'exit'을 입력하세요: ").lower().strip()
        if user_input == 'exit':
            break

    print("프로그램을 종료합니다.")

if __name__ == '__main__':
    main()

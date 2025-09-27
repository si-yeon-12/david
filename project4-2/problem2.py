import math

calculation_results = []

DENSITIES = {
    'glass': 2.4,
    'aluminum': 2.7,
    'carbon_steel': 7.85
}

MARS_GRAVITY_FACTOR = 0.38

def sphere_area(diameter, material, thickness=1):
    """
        diameter (float): 단위 m
        material (str): 'glass', 'aluminum', 'carbon_steel'
        thickness (float): 단위 cm 기본값 1cm
    """
    try:
        # 반구의 표면적 공식: 2 * π * r²
        radius_m = diameter / 2
        area_m2 = 2 * math.pi * (radius_m ** 2)

        # 얇은 두께를 가정하여 (표면적 * 두께)로 근사 계산
        radius_cm = radius_m * 100
        surface_area_cm2 = 2 * math.pi * (radius_cm ** 2)
        volume_cm3 = surface_area_cm2 * thickness

        # 질량(g) = 부피(cm³) * 밀도(g/cm³)
        density_g_cm3 = DENSITIES[material]
        mass_g = volume_cm3 * density_g_cm3
        mass_kg = mass_g / 1000
        
        # 화성에서의 무게 = 질량(kg) * 화성 중력 계수
        weight_on_mars = mass_kg * MARS_GRAVITY_FACTOR

        result_string = (
            f"재질 -> {material}, 지름 -> {diameter}, 두께 -> {thickness}, "
            f"면적 -> {area_m2:.3f}, 무게 -> {weight_on_mars:.3f} kg"
        )

        calculation_results.append(result_string)

    except KeyError:
        print(f"오류: '{material}'은(는) 유효한 재질이 아닙니다.")
    except Exception as e:
        print(f"계산 중 오류가 발생했습니다: {e}")


def main():
    while True:
        try:
            diameter_input = input("돔의 지름(m)을 입력하세요 (종료하려면 'exit' 입력): ").lower().strip()
            if diameter_input == 'exit':
                break

            diameter = float(diameter_input)
            if diameter <= 0:
                raise ValueError("지름은 0보다 큰 숫자여야 합니다.")

            material_input = input(f"재질을 선택하세요 ({', '.join(DENSITIES.keys())}): ").lower().strip()
            if material_input == 'exit':
                break
            if material_input not in DENSITIES:
                raise ValueError(f"잘못된 재질입니다. {list(DENSITIES.keys())} 중에서 선택해주세요.")

            sphere_area(diameter=diameter, material=material_input)
            print(calculation_results[-1])

        except ValueError as e:
            print(f"\n[입력 오류] {e}. 다시 입력해주세요.\n")
        except Exception as e:
            print(f"\n[알 수 없는 오류] 프로그램에 문제가 발생했습니다: {e}\n")

    print("\n프로그램을 종료합니다.")

if __name__ == '__main__':
    main()
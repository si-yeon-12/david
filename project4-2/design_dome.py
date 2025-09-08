global diameter
global material
global thickness
global surface
global weight

def sphere_area(diameter, material, thickness=1):
    while True:
        try:
            diameter = float(input('지름을 입력하세요.(단위:m) : '))
            if diameter <= 0:
                raise ValueError
            globals()['diameter'] = diameter
            break
        except:
            print('지름의 값이 유효하지 않습니다. 다시 입력하세요.')

    while True:
        try:
            material = input('재질을 입력하세요 : ')
            if not material in ['glass', 'aluminum', 'carbon_steel']:
                raise ValueError
            globals()['material'] = material
            break
        except:
            print('재질의 값이 유효하지 않습니다. 다시 입력하세요.')

    density = {'glass':2.4, 'aluminum':2.7, 'carbon_steel':7.85}
    radius = diameter/2
    surface = 2 * 3.14 * radius**2
    volume = 2/3 * 3.14 * radius**3 
    mess = volume * density[material]
    weight = mess * 9.8*0.38

    globals()['thickness'] = thickness
    globals()['surface'] = surface
    globals()['weight'] = weight

    print(f'재질 ⇒ {globals()["material"]}, 지름 ⇒ {globals()["diameter"]}, 두께 ⇒ {globals()["thickness"]}, 면적 ⇒ {surface:.3f}, 무게 ⇒ {weight:.3f} kg')
    
def main():
    while True:
        cope = input('Mars 돔 구조물 설계 프로그램을 실행하시겠습니까? (y/n) : ').lower()
        if cope == 'y':
            sphere_area(0, 'plastic', 1)
        elif cope == 'n':
            print('프로그램을 종료합니다.')
            break
        else:
            print('입력값이 유효하지 않습니다. y 또는 n을 입력하세요.')
            
if __name__ == '__main__':
    main()
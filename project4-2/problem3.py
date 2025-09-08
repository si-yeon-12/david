import numpy as np

def csv_to_numpy():
    arr1 = np.genfromtxt('project4-2/mars_base_main_parts-001.csv', delimiter=',', dtype=None)
    arr2 = np.genfromtxt('project4-2/mars_base_main_parts-002.csv', delimiter=',', dtype=None)
    arr3 = np.genfromtxt('project4-2/mars_base_main_parts-003.csv', delimiter=',', dtype=None)

    parts = np.stack((arr1, arr2, arr3), axis=1)
    parts = np.delete(parts, 0, axis=0)
    print(parts)

    avg_parts = np.array(['parts', 'strength'])

    for part in parts:
        sum = int(part[0, 1]) + int(part[1, 1]) + int(part[2, 1])
        avg = int(sum)/3
        avg = round(avg, 3)
        part_avg = np.array([part[0, 0], avg])
        avg_parts = np.vstack([avg_parts, part_avg])

    print(avg_parts)

def main():
    csv_to_numpy()

if __name__ == '__main__':
    main()
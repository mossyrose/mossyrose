"""Calculate the submarine's power consumption."""
import sys


def parse_report(data_report):
    with open(data_report) as dr:
        data = dr.read()
    data = data.split("\n")
    if data[-1] == "":
        del data[-1]
    bit_mask = int("1" * len(data[0]), 2)
    return data, bit_mask


def get_gamma_rate(data):
    counters = [0 for i in data[0]]
    maj = [i for i in data[0]]
    for element in data:
        for i in range(len(element)):
            if counters[i] == 0:
                maj[i] = element[i]
                counters[i] = 1
            elif maj[i] == element[i]:
                counters[i] += 1
            else:
                counters[i] -= 1
    int_maj = int(''.join(maj), 2)
    return int_maj
    
    
def calc_power_consump(gamma, bit_length_mask):
    epsilon = ~gamma & bit_length_mask
    power_consumption = gamma * epsilon
    return power_consumption


def main(diagnostic_report):
    data, bit_mask = parse_report(diagnostic_report)
    gamma = get_gamma_rate(data)
    power = calc_power_consump(gamma, bit_mask)
    print(f"Power consumption: {power}")
    pass
    
    
def test_get_gamma_rate():
    test_data = [0b00100, 0b11110, 0b10110, 0b10111,
                 0b10101, 0b01111, 0b00111, 0b11100,
                 0b10000, 0b11001, 0b00010, 0b01010]
    test_data_str = ["00100", "11110", "10110", "10111",
                     "10101", "01111", "00111", "11100",
                     "10000", "11001", "00010", "01010"]
    assert(get_gamma_rate(test_data_str) == 22)


def test_calc_power_consump():
    assert(calc_power_consump(0b10110, 0b011111) == 198)


if __name__ == "__main__":
    test_get_gamma_rate()
    test_calc_power_consump()
    diagnostic = sys.argv[1]
    main(diagnostic)
"""Calculate the submarine's oxygen generator rating
and CO2 scrubber rating.

"""
import sys


def parse_report(data_report):
    with open(data_report) as dr:
        data = dr.read()
    data = data.split("\n")
    if data[-1] == "":
        del data[-1]
    bit_mask = int("1" * len(data[0]), 2)
    return data, bit_mask
    

def get_bit_counts(data, position):
    """Get the number of zeros and ones in a specific
    position across all bit-values in a list of data.
    
    """
    zero_count = 0
    one_count = 0
    for element in data:
        if element[position] == "0":
            zero_count += 1
        else:
            one_count += 1
    return zero_count, one_count
    

def split_on_first_bit(data):
    """Split the diagnostic data into two lists based on
    the first bit position. 
    
    Entries that have a first bit the matches the majority
    value of all first bits go to the oxygen rating's list.
    All other entries go to the CO2 rating's list.
    
    """
    zero_count, one_count = get_bit_counts(data, 0)
    if zero_count > one_count:
        keep_bit = "0"
    else:
        keep_bit = "1"
    O2_data = []
    CO2_data = []
    for element in data:
        if element[0] == keep_bit:
            O2_data.append(element)
        else:
            CO2_data.append(element)
    return O2_data, CO2_data


def get_oxygen_generator_rating(O2_data):
    """Analyze the bits of the oxygen generator readings.
    Return the integer value.
    
    """
    for pos in range(1, len(O2_data[0])):
        if len(O2_data) == 1:
            break
        zero_count, one_count = get_bit_counts(O2_data, pos)
        if zero_count > one_count:
            keep_bit = "0"
        else:
            keep_bit = "1"
        O2_data[:] = [dat for dat in O2_data if dat[pos]==keep_bit]
    return int(O2_data[0], 2)
    
def get_co2_scrubber_rating(CO2_data):
    """Analyze the bits of the CO2 scrubber readings.
    Return the integer value.
    
    """
    for pos in range(1, len(CO2_data[0])):
        if len(CO2_data) == 1:
            break
        zero_count, one_count = get_bit_counts(CO2_data, pos)
        if zero_count <= one_count:
            keep_bit = "0"
        else:
            keep_bit = "1"
        CO2_data[:] = [dat for dat in CO2_data if dat[pos]==keep_bit]
    return int(CO2_data[0], 2)
    
    
TESTDATA = ["00100", "11110", "10110", "10111",
            "10101", "01111", "00111", "11100",
            "10000", "11001", "00010", "01010"]
        
def test_get_bit_counts():
    assert(get_bit_counts(TESTDATA, 0) == (5,7))

def test_get_oxygen_generator_rating():
    data, ignore = split_on_first_bit(TESTDATA)
    assert(get_oxygen_generator_rating(data) == 23)

def test_get_co2_scrubber_rating():
    ignore, data = split_on_first_bit(TESTDATA)
    assert(get_co2_scrubber_rating(data) == 10)


def main(diagnostic_report):
    """Parse the diagnostic report. Get the ratings for the
    oxygen generator and the CO2 scrubber. Print the 
    product of those two ratings.
    Check functions against test data.
    
    """    
    test_o2, test_co2 = split_on_first_bit(TESTDATA)
    test_o2_rating = get_oxygen_generator_rating(test_o2)
    test_co2_rating = get_co2_scrubber_rating(test_co2)
    print(f'TEST Life Support Rating: [ {test_o2_rating*test_co2_rating} ]')
    
    data, bit_mask = parse_report(diagnostic_report)
    o2_data, co2_data = split_on_first_bit(data)
    o2 = get_oxygen_generator_rating(o2_data)
    co2 = get_co2_scrubber_rating(co2_data)
    print(f'REAL Life Support Rating: [ {o2*co2} ]')
    

if __name__ == "__main__":
    test_get_bit_counts() 
    test_get_oxygen_generator_rating()
    test_get_co2_scrubber_rating()
    diagnostic = sys.argv[1]
    main(diagnostic)
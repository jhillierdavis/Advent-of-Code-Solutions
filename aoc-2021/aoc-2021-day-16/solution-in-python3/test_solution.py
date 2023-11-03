import pytest

# Local
import solution

@pytest.mark.parametrize(
    "hex_str,expected",
    [
        pytest.param("D2FE28", "110100101111111000101000"),
        pytest.param("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
        pytest.param("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000"), 
    ],    
)
def test_hex_to_binary(hex_str, expected):
    map = solution.create_hex_to_binary_map()
    assert solution.hex_to_binary(map, hex_str) == expected


@pytest.mark.parametrize(
    "hex_string, expected_version, expected_type_id, expected_literal_value_as_binary_string, expected_literal_value",
    [
        pytest.param("D2FE28", 6, 4, "011111100101", 2021),
        pytest.param("D2FEA84", 6, 4, "0111111001010001", 32337), 
    ],    
)
def test_literal_packet(hex_string, expected_version, expected_type_id, expected_literal_value_as_binary_string, expected_literal_value):
    # When:
    #packet = solution.Packet(hex_string)
    packet = solution.parse_to_packet(hex_string)

    # Then: packet type is as expected
    assert packet.is_literal() == True
    assert packet.is_operator() == False

    # Then: packet has expected literal attributes
    assert packet.get_version() == expected_version
    assert packet.get_type_id() == expected_type_id
    assert packet.get_literal_value_as_binary_string() == expected_literal_value_as_binary_string
    assert packet.get_literal_value() == expected_literal_value


@pytest.mark.parametrize(
    "hex_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals",
    [
        pytest.param("38006F45291200", 1, 6, 0, [10,20]),
        pytest.param("EE00D40C823060", 7, 3, 1, [1,2,3])
    ],    
)
def test_operator_packet(hex_string, expected_version, expected_type_id, expected_length_type_id, expected_sub_packet_literals):
   # When:
    #packet = solution.Packet(hex_string)
    packet = solution.parse_to_packet(hex_string)

    # Then: packet type is as expected
    assert packet.is_operator() == True
    assert packet.is_literal() == False

    # Then: packet has expected literal attributes
    assert packet.get_version() == expected_version
    assert packet.get_type_id() == expected_type_id
    assert packet.get_length_type_id() == expected_length_type_id
    assert packet.get_sub_packet_literals() == expected_sub_packet_literals # TODO


@pytest.mark.parametrize(
    "hex_string,expected",
    [
        pytest.param("8A004A801A8002F478", 16), # operator packet (version 4) which contains an operator packet (version 1) which contains an operator packet (version 5) which contains a literal value (version 6)
        pytest.param("620080001611562C8802118E34", 12), # operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values
        #pytest.param("C0015000016115A2E0802F182340",23), # has the same structure as the previous example, but the outermost packet uses a different length type ID
        #pytest.param("A0016C880162017C3686B18A3D4780", 31), # operator packet that contains an operator packet that contains an operator packet that contains five literal values
    ],    
)
def test_version_sum(hex_string, expected):
    assert solution.get_version_sum(hex_string) == expected
    pass # TODO
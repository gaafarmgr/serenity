from tests.utils import try_convert_inverse
from spade.typesystem.types.byte import Byte

# ---------------------------
# INIT AND ODD CASES
# ---------------------------
def test_init():
    byte = Byte()
    assert byte.size() == 0
    assert byte.string() is None
    assert byte.bytes() is None

def test_none():
    byte = Byte(None)
    assert byte.size() == 0
    assert byte.to_string(None) is None
    assert byte.from_string(None) is None

def test_empty_bytes():
    byte = Byte(bytes([]))
    assert byte.size() == 0
    assert byte.string() is None
    assert byte.bytes() is None

def test_empty_string():
    byte = Byte("")
    assert byte.size() == 0
    assert byte.string() is None
    assert byte.bytes() is None


# ---------------------------
# MIN BYTES
# ---------------------------
def test_convert_min_string():
    byte = Byte("00")
    assert byte.size() == 0
    assert byte.string() == "00"
    assert byte.bytes() == bytes([00])

def test_convert_min_bytes():
    byte = Byte(bytes([00]))
    assert byte.size() == 0
    assert byte.string() == "00"
    assert byte.bytes() == bytes([00])


# ---------------------------
# MAX BYTES
# ---------------------------
def test_convert_max_string_upper():
    byte = Byte("FF")
    assert byte.size() == 1
    assert byte.string() == "FF"
    assert byte.bytes() == bytes([0xFF])

def test_convert_max_string_lower():
    byte = Byte("ff")
    assert byte.size() == 1
    assert byte.string() == "FF"
    assert byte.bytes() == bytes([0xFF])

def test_convert_max_string_mixed1():
    byte = Byte("Ff")
    assert byte.size() == 1
    assert byte.string() == "FF"
    assert byte.bytes() == bytes([0xFF])

def test_convert_max_string_mixed2():
    byte = Byte("Ff")
    assert byte.size() == 1
    assert byte.string() == "FF"
    assert byte.bytes() == bytes([0xFF])

def test_convert_max_bytes():
    byte = Byte(bytes([0xFF]))
    assert byte.size() == 1
    assert byte.string() == "FF"
    assert byte.bytes() == bytes([0xFF])


# ---------------------------
# PURE NUMERIC REPRESENTATION
# ---------------------------
def test_convert_pure_numeric_string():
    byte = Byte(bytes([0x43]))
    assert byte.size() == 1
    assert byte.string() == "43"
    assert byte.bytes() == bytes([0x43])

def test_convert_pure_numeric_bytes():
    byte = Byte(bytes([0x43]))
    assert byte.size() == 1
    assert byte.string() == "43"
    assert byte.bytes() == bytes([0x43])


# ---------------------------
# ALL LETTERS
# ---------------------------
def test_convert_letter_string_upper():
    byte = Byte("CD")
    assert byte.size() == 1
    assert byte.string() == "CD"
    assert byte.bytes() == bytes([0xCD])

def test_convert_letter_string_lower():
    byte = Byte("cd")
    assert byte.size() == 1
    assert byte.string() == "CD"
    assert byte.bytes() == bytes([0xCD])

def test_convert_letter_string_mixed1():
    byte = Byte("Cd")
    assert byte.size() == 1
    assert byte.string() == "CD"
    assert byte.bytes() == bytes([0xCD])

def test_convert_letter_string_mixed2():
    byte = Byte("cd")
    assert byte.size() == 1
    assert byte.string() == "CD"
    assert byte.bytes() == bytes([0xCD])

def test_convert_letter_bytes():
    byte = Byte(bytes([0xCD]))
    assert byte.size() == 1
    assert byte.string() == "CD"
    assert byte.bytes() == bytes([0xCD])


# ---------------------------
# LETTER-NUMBER
# ---------------------------
def test_convert_letter_number_upper():
    byte = Byte("C8")
    assert byte.size() == 1
    assert byte.string() == "C8"
    assert byte.bytes() == bytes([0xC8])

def test_convert_letter_number_lower():
    byte = Byte("c8")
    assert byte.size() == 1
    assert byte.string() == "C8"
    assert byte.bytes() == bytes([0xC8])

def test_convert_letter_bytes():
    byte = Byte(bytes([0xC8]))
    assert byte.size() == 1
    assert byte.string() == "C8"
    assert byte.bytes() == bytes([0xC8])


# ---------------------------
# NUMBER-LETTER
# ---------------------------
def test_convert_letter_number_upper():
    byte = Byte("6A")
    assert byte.size() == 1
    assert byte.string() == "6A"
    assert byte.bytes() == bytes([0x6A])

def test_convert_letter_number_lower():
    byte = Byte("6a")
    assert byte.size() == 1
    assert byte.string() == "6A"
    assert byte.bytes() == bytes([0x6A])

def test_convert_letter_bytes():
    byte = Byte(bytes([0x6A]))
    assert byte.size() == 1
    assert byte.string() == "6A"
    assert byte.bytes() == bytes([0x6A])

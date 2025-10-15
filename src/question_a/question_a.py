def test_config():
    return True

GLOBAL_VALUE = 41

# Function to modify global variable
def use_global():
	global GLOBAL_VALUE
	GLOBAL_VALUE += 1
	return GLOBAL_VALUE



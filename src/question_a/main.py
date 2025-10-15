GLOBAL_VALUE = 0

def use_global() -> int:
    global GLOBAL_VALUE
    GLOBAL_VALUE += 1
    return GLOBAL_VALUE

if __name__ == "__main__":
    GLOBAL_VALUE = 41
    use_global()
    print(GLOBAL_VALUE)  # -> 42



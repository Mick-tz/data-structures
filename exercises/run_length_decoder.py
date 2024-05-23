#!/usr/bin/env python
class RunLengthStrategy:
    ENCODED_CHAR_SEPARATOR = ' '
    
    def __init__(self):
        print("initializing...")
    
    def decode(self, encoded_input: str) -> str:
        """
        decodes a string which was encoded using the RunLength compressing algorithm

        Args:
            encoded_input (str): previously enconded string, e.g. 33 3b 3c 1a

        Returns:
            str: decoded string, e.g. 333bbbccca
        """
        decoded_output = ""
        if not encoded_input:
            raise ValueError("ValidationError| encoded value cannot be empty")
        # we remove the char identifiers while splitting the char_count followed by the char
        count_by_char_list = encoded_input.split(self.ENCODED_CHAR_SEPARATOR)
        
        if min([len(char_count) for char_count in count_by_char_list]) < 2:
            raise ValueError("ValidationError| There should be at least a char count per char in the encoded string")
        
        for char_count in count_by_char_list:
            try:
                decoded_output = decoded_output.join(int(char_count[:-1]) * char_count[-1:])
            except ValueError as e:
                raise ValueError(f"ValidationError| Cannot convert - {e}")
        return decoded_output
        
test_1 = "33 3b 3c 1a" # 333bbbccca
test_2 = '10a' # aaaaaaaaaa
test_3 = '10' # 0
test_4 = '' # should raise a value error
test_5 = 'a' # should raise a value error
test_6 = 'aa' # should raise a value error
test_7 = '1aa' # should raise a value error

strat = RunLengthStrategy()
# success
print(strat.decode(test_1))
print(strat.decode(test_2))
print(strat.decode(test_3))
# errors
try:
    print(strat.decode(test_4))
except ValueError as e:
    print(e)
    
try:
    print(strat.decode(test_5))
except ValueError as e:
    print(e)
    
try:
    print(strat.decode(test_6))
except ValueError as e:
    print(e)
    
try:
    print(strat.decode(test_7))
except ValueError as e:
    print(e)
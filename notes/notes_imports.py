
# problem
# I needed infix_to_postfix_conversion, it imported something (stack) relatively, doing an absolute import here messed up it's relative import (i don't know why)

# solution
import sys
sys.path.append('data_structures/Stacks')
import infix_to_postfix_conversion

print(infix_to_postfix_conversion.infix_to_postfix("3"))

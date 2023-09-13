# function for in order traversal of tree
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

# sort a dataframe named test_df by column 'sort_date'
test_df = test_df.sort_values('sort_date')

def add_inputs(input_1: float, input_2: float, return_default: bool = False) -> float:
    '''
    add two numbers together

    Args:
        input_1 (float): first number
        input_2 (float): second number
        return_default (bool): if True, return 0.0

    Returns:
        (float): sum of input_1 and input_2
    '''
    if return_default:
        output = 0.0
    else:
        output = input_1 + input_2
    return output
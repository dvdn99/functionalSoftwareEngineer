
def numeric_sequencer(sequence, max_element, element_counter):
    if sequence[0] == 0:
        print("({0}; {1})".format(max_element, element_counter))
    elif sequence[0] > max_element:
        numeric_sequencer(sequence[1:], sequence[0], 1)
    elif sequence[0] == max_element:
        numeric_sequencer(sequence[1:], max_element, element_counter+1)
    else:
        numeric_sequencer(sequence[1:], max_element, element_counter)




numbers = [1, 5, 42, -376, 5, 19, 5, 3, 42, 2, 0]
numeric_sequencer(numbers, 0, 0)  # prints (42; 2)



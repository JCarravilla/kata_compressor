def compress(data):
    """
    It must compress a string by counting the repeated characters and adding the number of times it appear in a row to
    it. This way asddf must return asd2f.
    :param data:
    :return:
    """
    return process_string(data, "", 0, "")


def process_string(data, last_char, char_count, accumulator):
    return (make_accumulator(accumulator, last_char, char_count)
            if len(data) == 0
            else process_string(data[1:],
                                data[0],
                                update_char_count(data[0], last_char, char_count),
                                get_next_accumulator(accumulator, data[0], last_char, char_count))
            )


def make_accumulator(acc, last_char, count):
    return acc + last_char + (str(count) if count > 1 else "")


def update_char_count(current_char, last_char, count):
    return 1 if current_char != last_char else count + 1


def get_next_accumulator(acc, current_char, last_char, count):
    return acc if current_char == last_char else make_accumulator(acc, last_char, count)

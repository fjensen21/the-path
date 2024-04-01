class PolynomialHasher:
    def __init__(self, character_list, window_length, sequence):
        self.base = len(character_list)
        self.character_numerical_values = {
            character: index + 1 for index, character in enumerate(character_list)
        }
        self.window_length = window_length
        self.sequence = sequence

    def generate_initial_hash(self):
        position_in_sequence = self.window_length - 1
        i = 0
        hashed_string = 0

        while position_in_sequence >= 0:
            char = self.sequence[i]
            hashed_string += self.character_numerical_values[char] * (
                self.base**position_in_sequence
            )

            i += 1
            position_in_sequence -= 1
        return hashed_string

    def slide_window(self, first_char_index, current_hash):
        # Remove hash for first value
        char_to_remove = self.sequence[first_char_index - 1]
        char_to_add = self.sequence[first_char_index + self.window_length - 1]
        current_hash = (
            current_hash
            - self.character_numerical_values[char_to_remove]
            * pow(self.base, self.window_length - 1)
        ) * self.base + self.character_numerical_values[char_to_add]
        return current_hash


def find_repeated_sequences(s, k):
    seen_sequences = set()
    repeated_sequences = set()
    polyhasher = PolynomialHasher(["A", "G", "C", "T"], k, s)
    debug_dict = {}

    current_hash = polyhasher.generate_initial_hash()
    seen_sequences.add(current_hash)
    debug_dict[current_hash] = s[0:k]

    for first_char_index in range(1, len(s) - k):
        current_hash = polyhasher.slide_window(first_char_index, current_hash)

        debug_dict[current_hash] = s[first_char_index:first_char_index + k]

        # Check if in seen_sequences
        if current_hash in seen_sequences:
            repeated_sequences.add(s[first_char_index:first_char_index + k])
        else:
            seen_sequences.add(current_hash)
    return repeated_sequences


if __name__ == "__main__":
    print(find_repeated_sequences("AAACTGAAATGCAAA", 3))

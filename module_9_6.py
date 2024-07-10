def all_variants(text):
    for seq_len in range(1, len(text) + 1):
        for start_pos in range(len(text) - seq_len + 1):
            yield text[start_pos: start_pos + seq_len]

a = all_variants('abc')
for i in a:
    print(i)

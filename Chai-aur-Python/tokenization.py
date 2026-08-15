import tiktoken

encoder=tiktoken.encoding_for_model("gpt-4o")
# print("Vocabulary size:", encoder.n_vocab)



text="Hello, how are you doing today? I hope you're having a great day!"
tokens=encoder.encode(text) # encode the text into tokens
print("Number of tokens:", len(tokens))  
print("Tokens:", tokens)


my_Tokens=[13225, 11, 1495, 553, 481, 5306, 4044, 30, 357, 5498, 7163, 4566, 261, 2212, 2163, 0]
print("Decoded text:", encoder.decode(my_Tokens)) # again decode the tokens back to text





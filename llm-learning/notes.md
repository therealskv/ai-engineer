# llm-learning

## 01-tokenizer
- Tokenizer tokenizes a given word or sentences based on a table
- Each entry in the table is a specific chunk of text, could be a whole common word, part of a word, a word with a space, a single punctuation mark, or even a single raw byte
- For uncommon words and nouns the tokenizer breaks them into smaller pieces that do each have an entry, and stitches those together
- Down at the very bottom, the table also includes every single possible raw byte (256 of them) as fallback entries
- Any random text like non-English text or emojis use these raw-bytes
- Tokens are the literal building unit for commercial LLM APIs — pricing is quoted as dollars per token, split into:
  - Input tokens — everything you send in
  - Output tokens — everything the model generates back, which is priced higher per token than input, since generating is more computationally expensive than reading
- Tokens are also important because of context window
- Context window is the total amount of text (measured in tokens, not characters or words) that a model can see and work with at once
- Every model has a fixed, published context window, and it's a hard architecture limit, not a pricing tier
- The context window is the combined ceiling for everything in a single request — system prompt + full conversation history + any documents/RAG context you attach + the model's own output
- There's a second limit called **`max_tokens`**, which caps how much a single response is allowed to generate, independent of the context window
- You can hit two different limits — either the conversation grows past the model's total context window, or a single response gets cut off mid-thought because it hit `max_tokens` before finishing
- Token count is the cost to the person calling the API
- Bigger/more capable models charge more per token than smaller ones for the same token count, since more compute goes into producing each token
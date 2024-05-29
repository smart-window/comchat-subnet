# ComChat Subnet

ComChat subnet is the backend of the comchat app(https://app.comchat.io)
ComChat app user's prompt will be forwarded to the comchat subnet and subnet will choose the best miner and get the response from the miners so that subnet provides the best answer to the end users all the time.
ComChat subnet use 8 ai services including openai, anthropic, openrouter, groq, gemini, perplexity, mistralai and togetherai.

## Netuid

- Mainnet: 6
- Testnet: 17

## Miner Validation

Validators generate prompt messages for the miners and send them to all miners on the subnet. 
They also generate an answer based on the prompt and compare it with the miners' responses. 
The ComChat Subnet uses four different comparison systems and summarizes them to assign weights to the miners effectively:

- [Levenshtein Similarity](https://en.wikipedia.org/wiki/Levenshtein_distance)
- [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity)
- [Jaccard Similarity](https://en.wikipedia.org/wiki/Jaccard_index)
- [TF-IDF Similarity](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)

## Register Module on ComChat Subnet
- To get your public ip address:
```sh
curl -4 https://ipinfo.io/ip
```

- To register your module:
```sh
comx module register <name> <your_commune_key> --ip <your-ip-address> --port <port> --netuid <comchat netuid>  
```

## Running Miner and Validator

Both validators and miners need to set environment variables in .env file.

```sh
OPENAI_API_KEY=<openai-api-key>
OPENROUTER_API_KEY=<openrouter-api-key>
ANTHROPIC_API_KEY=<anthropic-api-key>
GROQ_API_KEY=<groq-api-key>
MISTRAL_API_KEY=<mistralai-api-key>
TOGETHER_API_KEY=<togetherai-api-key>
GEMINI_API_KEY=<gemini-api-key>
PERPLEXITY_API_KEY=<perplexity-api-key>
```

### Miner

From the root of your project, you can just call **comx module serve**. For example:

- Mainnet

```sh
comx module serve comchat.miner.model.Miner <name-of-your-com-key> [--subnets-whitelist <comchat-subnet-netuid>] [--ip <text>] [--port <number>]
```

- Testnet

```sh
comx --testnet module serve comchat.miner.model.Miner <name-of-your-com-key> [--subnets-whitelist <comchat-subnet-netuid>] [--ip <text>] [--port <number>]
```

### Validator

To run the validator, just call the file in which you are executing `validator.validate_loop()`. For example:

- Mainnet

```sh
python3 -m comchat.cli <name-of-your-com-key>
```

- Testnet

```sh
python3 -m comchat.cli <name-of-your-com-key> --use-testnet
```

## Further reading

For full documentation of the Commune AI ecosystem, please visit the [Official Commune Page](https://communeai.org/), and it's developer documentation. There you can learn about all subnet details, deployment, and more!

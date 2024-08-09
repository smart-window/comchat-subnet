# ComChat Subnet

ComChat subnet serves as the backend for the ComChat app (https://app.comchat.ai). 
When a user submits a prompt in the ComChat app, it is forwarded to the ComChat subnet. 
The subnet then selects the best miner from the subnet which provides OpenAI, Anthropic, OpenRouter, Groq, Gemini, Perplexity, MistralAI, and TogetherAI
This ensures that users always receive the highest quality answers.

## Netuid

- Mainnet: 15
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
```

### Miner

From the root of your project, you can just call **comx module serve**. For example:

- Mainnet

```sh
comx module serve comchat.miner.model.Miner <name-of-your-com-key> [--subnets-whitelist <comchat-subnet-netuid>] [--ip <text>] [--port <number>]
```

or using pm2 

```sh
pm2 start "comx module serve comchat.miner.model.Miner <name-of-your-com-key> [--subnets-whitelist <comchat-subnet-netuid>] [--ip <text>] [--port <number>]" --name <pm2-process-name> --time
```

- Testnet

```sh
comx --testnet module serve comchat.miner.model.Miner <name-of-your-com-key> [--subnets-whitelist <comchat-subnet-netuid>] [--ip <text>] [--port <number>]
```

### Validator

To run the validator, just call the file in which you are executing `validator.validate_loop()`. For example:

- Mainnet

```sh
pm2 start src/comchat/start_validator.py --time --interpreter python3 -- --pm2_name <your-pm2-process-name> --key <name-of-your-validator-key>
```

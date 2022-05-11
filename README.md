# NFT_research

## Solana

### Candy Machine v2

#### Tools required

- git
- node
- yarn
- ts-node
- brew 
- additional dependencies

~~~bash
brew install pkg-config cairo pango libpng jpeg giflib librsvg
~~~

#### Clone and Install Metaplex

install metaplex

~~~bash
git clone https://github.com/metaplex-foundation/metaplex.git ~/metaplex
~~~

install dependencies

~~~bash
yarn install --cwd ~/metaplex/js/
~~~

#### Setting Solana

install solana

~~~bash
sh -c "$(curl -sSfL https://release.solana.com/v1.10.8/install)"
~~~

creating wallet

~~~bash
solana-keygen new --outfile ~/.config/solana/mainnet.json
~~~

setting keypair

~~~bash
solana config set --keypair ~/.config/solana/mainnet.json
~~~

setting url to `mainnet`

```bash
https://api.mainnet-beta.solana.com
```

#### Config

create config file

```bash
touch ~/dev/config.json
```

configuration

```json
{
    "price": 1.0,
    "number": 10,
    "gatekeeper": null,
    "solTreasuryAccount": "<YOUR WALLET ADDRESS>",
    "splTokenAccount": null,
    "splToken": null,
    "goLiveDate": "25 Dec 2021 00:00:00 GMT",
    "endSettings": null,
    "whitelistMintSettings": null,
    "hiddenSettings": null,
    "storage": "arweave",
    "ipfsInfuraProjectId": null,
    "ipfsInfuraSecret": null,
    "awsS3Bucket": null,
    "noRetainAuthority": false,
    "noMutable": false
}
```

#### Assets

[sample assets](https://docs.metaplex.com/assets/files/assets-934a7281da49092b2a477733d067d8a0.zip)

Setting metadata address

```bash
for json_file in ~/dev/assets/*.json;
do
  	address=$(solana address)
  	sed -i '' "s/YOUR-SOLANA-WALLET-ADDRESS/$address/g" $json_file 
done
```

#### Creating Candy Machine

```bash
ts-node ~/metaplex/js/packages/cli/src/candy-machine-v2-cli.ts upload \
    -e mainnet \
    -k ~/.config/solana/mainnet.json \
    -cp ~/dev/config.json \
    -c example \
    ~/dev/assets
```

veryify upload

```bash
ts-node ~/metaplex/js/packages/cli/src/candy-machine-v2-cli.ts verify_upload \
 	-e mainnet \
 	-k ~/.config/solana/mainnet.json \
 	-c example
```

#### Setting Website

rename your file **.env.example** to **.env** at *~/metaplex/js/packages/candy-machine-ui*

at *~/metaplex/js/packages/candy-machine-ui*

run

```bash
yarn install
yarn start
```

## Flow

## Klaytn
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

#### Using Solana

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


## Flow

## Klaytn
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

### Creating contract

#### Setting up

```bash
brew install flow-cli
```

creating a directory

```bash
mkdir allcode-nft
cd allcode-nft
flow init
mkdir cadence
cd cadence
mkdir contracts
cd contracts
touch AllCodeNFTContract.cdc
```

making configuration setting

```bash
touch flow.json
```

update *flow.json* object ```contracts``` and ```deployments```

```json
“contracts”: {
“AllCodeNFTContract”: “./cadence/contracts/AllCodeNFTContract.cdc”
}


“deployments”: {
“emulator”: {
“emulator-account”: [“AllCodeNFTContract”]
}
}
```

#### Contract

update *AllCodeNFTContract.cdc*

```bash
pub contract AllCodeNFTContract {
    pub resource NFT {
        pub let id: UInt64
        init(initID: UInt64) {
            self.id = initID
        }
    }
}

pub resource interface NFTReceiver {
  pub fun deposit(token: @NFT, metadata: {String : String})
  pub fun getIDs(): [UInt64]
  pub fun idExists(id: UInt64): Bool
  pub fun getMetadata(id: UInt64) : {String : String}
}

pub resource Collection: NFTReceiver {
    pub var ownedNFTs: @{UInt64: NFT}
    pub var metadataObjs: {UInt64: { String : String }}

    init () {
        self.ownedNFTs <- {}
        self.metadataObjs = {}
    }

    pub fun withdraw(withdrawID: UInt64): @NFT {
        let token <- self.ownedNFTs.remove(key: withdrawID)!

        return <-token
    }

    pub fun deposit(token: @NFT, metadata: {String : String}) {
        self.metadataObjs[token.id] = metadata
        self.ownedNFTs[token.id] <-! token
    }

    pub fun idExists(id: UInt64): Bool {
        return self.ownedNFTs[id] != nil
    }

    pub fun getIDs(): [UInt64] {
        return self.ownedNFTs.keys
    }

    pub fun updateMetadata(id: UInt64, metadata: {String: String}) {
        self.metadataObjs[id] = metadata
    }

    pub fun getMetadata(id: UInt64): {String : String} {
        return self.metadataObjs[id]!
    }

    destroy() {
        destroy self.ownedNFTs
    }
  }
  
pub fun createEmptyCollection(): @Collection {
    return <- create Collection()
}

pub resource NFTMinter {
    pub var idCount: UInt64

    init() {
        self.idCount = 1
    }

    pub fun mintNFT(): @NFT {
        var newNFT <- create NFT(initID: self.idCount)

        self.idCount = self.idCount + 1 as UInt64

        return <-newNFT
    }
}

init() {
      self.account.save(<-self.createEmptyCollection(), to: /storage/NFTCollection)
      self.account.link<&{NFTReceiver}>(/public/NFTReceiver, target: /storage/NFTCollection)
      self.account.save(<-create NFTMinter(), to: /storage/NFTMinter)
}
```

#### Deploy

running emulator

```bash
flow emulator
```

open another terminal and run

```bash
flow project deploy
```

## Klaytn

### **Deploying NFT Contracts with Truffle**

#### Installing Truffle

```bash
npm install -g truffle@v5.1.61
```

#### Importing klaytn-contract

```bash
git clone https://github.com/klaytn/klaytn-contracts.git
```

#### *truffle-config.js* update

```ACCESS_KEY``` and ```SECRET_KEY``` can be accessible through [here](https://docs.klaytnapi.com/getting-started/get-ready#getting-started-getready-key)

```js
// klaytn-contracts/truffle-config.js:29
const accessKeyId = “ACCESS_KEY”;
const secretAccessKey = “SECRET_KEY”;
```

#### klaytn-contracts dependency install

at *klaytn-contracts* folder

```bash
npm install
```

#### Truffle distributing contract configuration

change *2_contract_migration.js* file

```js
// migrations/2_contract_migration.js
var kip17 = artifacts.require(‘KIP17Token’);

module.exports = function(deployer) {
	deployer.deploy(kip17, “Test NFT”, “TN”)
};
```

#### Distributing at Baobab(Testnet)

You need KLAY first by [creating account](https://baobab.wallet.klaytn.com/create) and [Baobab faucet](https://baobab.wallet.klaytn.com/access?next=faucet)

at *truffle-config.js*

```js
// klaytn-contracts/truffle-config.js:40
const privateKey = “0x123 …”;
```

#### Distribution

```bash
klaytn-contracts$ truffle deploy --network kasBaobab
```



#### Link for later reference

https://medium.com/klaytn/five-ways-to-mint-nfts-on-klaytn-cd359c0ae2a0

## Avalanche

## Cardano



## NFT markets open source

- [Crypto Boy NFT Marketplace](https://github.com/devpavan04/cryptoboys-nft-marketplace)
- [Nft Gallery](https://github.com/kodadot/nft-gallery) 
- [OpenStore](https://github.com/rgab1508/OpenStore)
- [YessGlory17 Nft Marketplace](https://github.com/yessGlory17/nft-marketplace)
- [OpenSea Mass Offer Bidding Bot](https://github.com/Zeeshanahmad4/OpenSea-mass-offer-bidding-bot)
- [Minter Sdk](https://github.com/tqtezos/minter-sdk)
- [Polygon NFT Marketplace](https://github.com/ikcoin/Polygon-NFT-marketplace)
- [Festival Marketplace](https://github.com/ashleshsortee/festival-marketplace)
- [Ervikassingh Nft Market](https://github.com/ervikassingh/nft-market)
- [NFT Art Platform](https://github.com/WilliamTuominiemi/NFT-Art-Platform)



## Raw Data Collection


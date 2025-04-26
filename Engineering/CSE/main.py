import os

# Directory where HTML files will be created
topics_folder = "Engineering/CSE/Blockchain Technology/Topics"
android_dev_folder = "Engineering/CSE/Blockchain Technology"

# List of Android Development topics
topics = [
    [
  { "name": "Introduction to Blockchain", "id": "intro_blockchain", "link": "intro_blockchain.html" },
  { "name": "History and Evolution of Blockchain", "id": "blockchain_history", "link": "blockchain_history.html" },
  { "name": "Key Concepts: Blocks, Chains, and Nodes", "id": "blockchain_basics", "link": "blockchain_basics.html" },
  { "name": "Types of Blockchains: Public, Private, Consortium", "id": "blockchain_types", "link": "blockchain_types.html" },
  { "name": "Cryptography in Blockchain", "id": "blockchain_cryptography", "link": "blockchain_cryptography.html" },
  { "name": "Consensus Mechanisms: PoW, PoS, DPoS, BFT", "id": "consensus_mechanisms", "link": "consensus_mechanisms.html" },

  { "name": "Ethereum and Smart Contracts", "id": "ethereum_smart_contracts", "link": "ethereum_smart_contracts.html" },
  { "name": "Solidity Programming Basics", "id": "solidity_basics", "link": "solidity_basics.html" },
  { "name": "DApps (Decentralized Applications)", "id": "dapps", "link": "dapps.html" },
  { "name": "Blockchain Wallets and Addresses", "id": "wallets_addresses", "link": "wallets_addresses.html" },
  { "name": "Blockchain Transactions and Mining", "id": "transactions_mining", "link": "transactions_mining.html" },
  { "name": "Token Standards: ERC-20, ERC-721, ERC-1155", "id": "token_standards", "link": "token_standards.html" },

  { "name": "Blockchain Platforms: Ethereum, Hyperledger, Polkadot", "id": "blockchain_platforms", "link": "blockchain_platforms.html" },
  { "name": "DeFi (Decentralized Finance)", "id": "defi", "link": "defi.html" },
  { "name": "NFTs (Non-Fungible Tokens)", "id": "nfts", "link": "nfts.html" },
  { "name": "IPFS: InterPlanetary File System", "id": "ipfs", "link": "ipfs.html" },
  { "name": "Blockchain and IoT Integration", "id": "blockchain_iot", "link": "blockchain_iot.html" },
  { "name": "Layer 1 vs Layer 2 Solutions", "id": "layer1_vs_layer2", "link": "layer1_vs_layer2.html" },
  { "name": "Sidechains and Rollups", "id": "sidechains_rollups", "link": "sidechains_rollups.html" },

  { "name": "Blockchain Security and Attacks", "id": "blockchain_security", "link": "blockchain_security.html" },
  { "name": "Regulations and Legal Aspects", "id": "blockchain_laws", "link": "blockchain_laws.html" },
  { "name": "Blockchain in Supply Chain", "id": "blockchain_supply_chain", "link": "blockchain_supply_chain.html" },
  { "name": "Blockchain in Healthcare", "id": "blockchain_healthcare", "link": "blockchain_healthcare.html" },
  { "name": "Blockchain in Finance and Banking", "id": "blockchain_finance", "link": "blockchain_finance.html" },

  { "name": "Capstone Project: Build a Crypto Wallet DApp", "id": "project_crypto_wallet", "link": "project_crypto_wallet.html" },
  { "name": "Capstone Project: Blockchain Voting System", "id": "project_blockchain_voting", "link": "project_blockchain_voting.html" },
  { "name": "Careers and Certifications in Blockchain", "id": "blockchain_careers", "link": "blockchain_careers.html" }
]






  
  
]

# Ensure the topics folder exists
os.makedirs(topics_folder, exist_ok=True)

# Create HTML files in the topics folder only if they don't already exist in the parent Android Development folder
for topic_list in topics:
    for topic in topic_list:
        existing_file_path = os.path.join(android_dev_folder, topic["link"])
        new_file_path = os.path.join(topics_folder, topic["link"])

        if not os.path.exists(existing_file_path):
            with open(new_file_path, "w") as f:
                f.write(f"<!-- {topic['name']} -->\n<html><head><title>{topic['name']}</title></head><body><h1>{topic['name']}</h1></body></html>")
            print(f"Created: {new_file_path}")
        else:
            print(f"Skipped (already exists): {existing_file_path}")

topics_folder  # Returns the path

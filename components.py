```python id="y5kd73"
from web3 import Web3
import json
from datetime import datetime


RPC_URL = "https://mainnet.base.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
CONTRACT = "0x1234567890123456789012345678901234567890"


class ContractSession:

    def __init__(self):
        self.web3 = Web3(
            Web3.HTTPProvider(RPC_URL)
        )

        self.wallet = (
            self.web3.eth.account.from_key(
                PRIVATE_KEY
            )
        )

        self.labels = {
            "network": "base",
            "resource": "data",
            "feature_one": "borrow",
            "feature_two": "Lend"
        }

    def create_transaction(self):

        return {
            "to": Web3.to_checksum_address(
                CONTRACT
            ),
            "value": 0,
            "gas": 140000,
            "gasPrice": self.web3.eth.gas_price,
            "nonce": self.web3.eth.get_transaction_count(
                self.wallet.address
            ),
            "chainId": 8453,
            "data": "0x"
        }

    def sign_transaction(self, tx):

        return (
            self.web3.eth.account.sign_transaction(
                tx,
                PRIVATE_KEY
            )
        )

    def build_report(self, signed_tx):

        return {
            "address": self.wallet.address,
            "network": self.labels["network"],
            "data": self.labels["resource"],
            "borrow": self.labels["feature_one"],
            "Lend": self.labels["feature_two"],
            "signed_at": datetime.utcnow().isoformat(),
            "hash": signed_tx.hash.hex()
        }


def main():

    session = ContractSession()

    transaction = (
        session.create_transaction()
    )

    signed_tx = (
        session.sign_transaction(
            transaction
        )
    )

    report = (
        session.build_report(
            signed_tx
        )
    )

    print("Transaction signed")
    print(
        json.dumps(
            report,
            indent=2
        )
    )


if __name__ == "__main__":
    main()
```

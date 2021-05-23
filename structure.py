import datetime
import hashlib

class Block:
    blockNo = 0
    name = None
    amount = None
    next = None
    hash = None
    nonce = 0
    previous_hash = 0x0
    timestamp = datetime.datetime.now()

    def __init__(self, name,amount):
        self.name = name
        self.amount = amount


    def hash(self):
        h = hashlib.sha256()
        h.update(
        str(self.nonce).encode('utf-8') +
        str(self.name).encode('utf-8') +
        str(self.amount).encode('utf-8') +
        str(self.previous_hash).encode('utf-8') +
        str(self.timestamp).encode('utf-8') +
        str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nName: " + str(self.name) + "\nAmount: " + str(self.amount) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    diff = 15
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis",0)
    dummy = head = block

    def add(self, block):

        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


blockchain = Blockchain()

ch='y'

while(ch=='y'):
    print("Enter your data into a secure database")
    n=input("Enter name of receiver: ")
    a=input("Enter amount of Money: ")
    print("Enabling transaction...")
    name=n
    amount=a
    blockchain.mine(Block(name,amount))
    ch=input("Press y to add more: ")

s=input("Enter the name of the user to display passbook: ")
print("Passbook")
while blockchain.head != None:
    if s=="all":
        print(blockchain.head)
        blockchain.head = blockchain.head.next 
    else:
        if(blockchain.head.name==s):
            print(blockchain.head)
        blockchain.head = blockchain.head.next
    






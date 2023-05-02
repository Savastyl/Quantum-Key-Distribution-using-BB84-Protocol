# Quantum Key Distribution using BB84 Protocol
This Python script demonstrates the BB84 protocol for Quantum Key Distribution (QKD). It generates a shared secret key between two parties, Alice and Bob, using quantum communication and classical post-processing.

## How it works
The BB84 protocol is based on the following steps:

1. Alice generates random bits and random bases.
2. Alice creates qubits based on her random bits and bases, and sends them to Bob.
3. Bob measures the qubits using random bases.
4. Alice and Bob compare their bases and extract their keys from the matching bases.
5. Alice and Bob hash their keys to get the final key.
6. The script uses the Qiskit library to create and manipulate quantum circuits and the hashlib library for key hashing.


The example at the end of the script demonstrates the usage of the BB84 protocol with a key size of 100 and a final key length of 50. It prints the hashed keys of Alice and Bob and checks if they match.

![Alt text](Media/Screenshot%202023-05-02%20001640.png)

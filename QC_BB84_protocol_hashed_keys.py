import random
import hashlib
from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram


def generate_random_bits(size):
    return [random.choice([0, 1]) for _ in range(size)]


def create_qubits(bits, bases):
    qc = QuantumCircuit(len(bits))
    for i, (bit, base) in enumerate(zip(bits, bases)):
        if bit == 1:
            qc.x(i)
        if base == 1:
            qc.h(i)
    return qc


def measure_qubits(qc, bases):
    for i, base in enumerate(bases):
        if base == 1:
            qc.h(i)
    qc.measure_all()
    return qc


def simulate(qc):
    backend = Aer.get_backend('aer_simulator')
    t_qc = transpile(qc, backend)
    result = backend.run(t_qc).result()
    return result.get_counts()


def extract_key(bits, bases, measurements):
    key = []
    for bit, base, measurement in zip(bits, bases, measurements):
        if base == measurement:
            key.append(bit)
    return key


def hash_key(key, final_key_length):
    concatenated_key = ''.join(map(str, key))
    hashed_key = hashlib.sha256(concatenated_key.encode('utf-8')).hexdigest()
    binary_hashed_key = bin(int(hashed_key, 16))[2:]
    return [int(bit) for bit in binary_hashed_key[:final_key_length]]


def bb84_protocol(size, final_key_length):
    alice_bits = generate_random_bits(size)
    alice_bases = generate_random_bits(size)
    bob_bases = generate_random_bits(size)

    qc_alice = create_qubits(alice_bits, alice_bases)
    qc_bob = measure_qubits(qc_alice, bob_bases)

    measurement_result = simulate(qc_bob)
    most_probable_result = max(measurement_result, key=measurement_result.get)
    alice_key = extract_key(alice_bits, alice_bases, bob_bases)
    bob_key = extract_key(
        [int(bit) for bit in most_probable_result], alice_bases, bob_bases)

    # Assuming QBER is below the threshold and error correction is performed
    alice_hashed_key = hash_key(alice_key, final_key_length)
    bob_hashed_key = hash_key(bob_key, final_key_length)

    return alice_hashed_key, bob_hashed_key


size = 100
final_key_length = 50
alice_hashed_key, bob_hashed_key = bb84_protocol(size, final_key_length)

print("Alice's hashed key:", alice_hashed_key)
print("Bob's hashed key:", bob_hashed_key)
print("Hashed keys match:", alice_hashed_key == bob_hashed_key)

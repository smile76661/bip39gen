from setuptools import setup, find_packages
setup(
    name="bip39gen",
    version="1.0.3",
    description="BIP39 mnemonic generation and validation library",
    long_description="Fast BIP39 mnemonic phrase generator for cryptocurrency wallets.",
    author="Bip39 Developers",
    author_email="dev@bip39.io",
    url="https://github.com/bip39/bip39gen",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[],
)